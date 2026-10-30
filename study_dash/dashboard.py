from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

from werkzeug.exceptions import abort

from study_dash.auth import login_required
from study_dash.service import get_service_container, GradeService, RecommendationService
from study_dash.dto import OverviewDTO, GradeDTO, SemesterDTO, ModuleDTO, EnrollmentDTO
from study_dash.auth import get_student
from study_dash.repository import EnrollmentRepository, ModuleRepository, ProgramRepository
from study_dash.entity import Enrollment

bp = Blueprint('blog', __name__)

def get_average_grade(enrollment: Enrollment):
    """Returns the average grade of a student."""
    grade_service = get_service_container().get_service(GradeService)
    grade = grade_service.calculate_student_average(enrollment=enrollment)
    color = grade_service.get_grade_color(grade=grade, target=enrollment.target_grade)
    return GradeDTO(grade=grade, color=color)


def get_semesters(enrollment: Enrollment) -> list[SemesterDTO]:
    """
    Returns a list of semesters with their respective modules.
    The Modules are dynamically distributed over the semesters, with excess modules being added to the first semesters.
    """
    module_repository = get_service_container().get_service(ModuleRepository)
    grade_service = get_service_container().get_service(GradeService)
    program_modules = module_repository.find_by_program_id(enrollment.program_id)
    
    step_size = len(program_modules) // enrollment.semesters
    remainder = len(program_modules) % enrollment.semesters

    sem_modules = [
    program_modules[
        i * step_size + min(i, remainder)
        :
        (i+1) * step_size + min(i+1, remainder)
    ]
    for i in range(enrollment.semesters)
    ]

    return [
        SemesterDTO(
            semester_nr=i + 1,
            modules=[
                ModuleDTO(
                    module=module, grade=grade_service.get_grade_for_module(enrollment=enrollment, module=module)
                    )
                for module in modules
            ])
        for i, modules in enumerate(sem_modules)
    ]

def get_grades(enrollment: Enrollment):
    """Returns a list of GradeDTO objects representing the grades for each module in an enrollment."""
    grade_service = get_service_container().get_service(GradeService)
    module_repository = get_service_container().get_service(ModuleRepository)

    grades_for_modules = grade_service.grades_for_modules(enrollment=enrollment)
    return [GradeDTO(
        module=module_repository.find_by_id(module_id),
        grade=grade,
        color=grade_service.get_grade_color(grade=grade, target=enrollment.target_grade)
        )
        for module_id, grade in grades_for_modules.items()
    ]


@bp.route('/')
@login_required
def index():
    """
    Show the dashboard for the current student.
    Changes the shown modules based on the selected enrollment.
    Shows the grades for each module in the selected enrollment.
    Shows recommendations based on the current grades and target grade.
    Shows recommendation for the next finish of a module.
    """
    student = get_student()
    enrollment_repository = get_service_container().get_service(EnrollmentRepository)
    recommendation_service = get_service_container().get_service(RecommendationService)
    program_repository = get_service_container().get_service(ProgramRepository)

    enrollments = enrollment_repository.find_by_student_id(student_id=student.id)
    enrollment_id = request.args.get('enrollment_id', type=int)
    if len(enrollments) == 0:
        return render_template('dashboard/index-no-enrollment.html.j2')

    if enrollment_id == None:
        # @todo check that enrollments is not empty
        enrollment = enrollments[0]
    else:
        enr = enrollment_repository.find_by_id(enrollment_id)
        if enr.student_id == student.id:
            enrollment = enr
        else:
            return render_template('dashboard/index-no-enrollment.html.j2')

    

    overview = OverviewDTO(
        average_grade=get_average_grade(enrollment=enrollment),
        semesters=get_semesters(enrollment=enrollment),
        student=student,
        enrollment=EnrollmentDTO(enrollment=enrollment, program=program_repository.find_by_id(enrollment.program_id)),
        enrollments=[EnrollmentDTO(enrollment=enrlmnt, program=program_repository.find_by_id(enrlmnt.program_id)) for enrlmnt in enrollments],
        grades=get_grades(enrollment=enrollment),
        next_modul_end=recommendation_service.calculate_recommended_end(enrollment=enrollment, target=enrollment.target_end_date is not None)
    )


    return render_template('dashboard/index.html.j2', overview=overview, enrollment_id=enrollment_id)