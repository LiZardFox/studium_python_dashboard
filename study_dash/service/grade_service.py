import statistics

from .service import Service, ServiceContainer
from study_dash.entity import Attempt, Student, Module, Enrollment
from study_dash.repository import EvaluationRepository, AttemptRepository

class GradeService(Service):
    """
    Service class for grade calculation.
    Extends the Service class.
    """

    DEFAULT_TARGET = 4.0
    DEVIATION = 0.2

    def __init__(self, service_container: ServiceContainer):
        self.evaluation_repository = service_container.get_service(EvaluationRepository)
        self.attempt_repository = service_container.get_service(AttemptRepository)

    def calculate_grade(self, attempt: Attempt) -> float:
        score = attempt.score
        evaluation = self.serviceContainer.get_service(EvaluationRepository).find_by_id(attempt.evaluation_id)
        max_score = evaluation.max_score
        percent = score / max_score * 100
        if(percent < 56):
            return 5.0
        elif(percent < 61):
            return 4.0
        elif(percent < 66):
            return 3.7
        elif(percent < 71):
            return 3.3
        elif(percent < 76):
            return 3.0
        elif(percent < 81):
            return 2.7
        elif(percent < 81):
            return 2.3
        elif(percent < 86):
            return 2.0
        elif(percent < 91):
            return 1.7
        elif(percent < 96):
            return 1.3
        else:
            return 1.0
    

    def __latest_graded_attempts(self, enrollment: Enrollment):
        """
            Returns a dict with the Evaluation Id as key and the most current graded attempt, based on the date_of_attempt property, as the value
        """
        attempts = self.attempt_repository.find_by_enrollment_id(enrollment.id)
        latest_graded_attempts: dict[int, Attempt] = {}
        for attempt in attempts:
            if not attempt.graded():
                continue

            latest_attempt = latest_graded_attempts.get(attempt.evaluation_id)
            if latest_attempt is None or attempt.date_of_attempt > latest_attempt.date_of_attempt:
                latest_graded_attempts[attempt.evaluation_id] = attempt
        return latest_graded_attempts


    def grades_for_modules(self, enrollment: Enrollment) -> dict[int, float]:
        module_grades: dict[int, float] = {}
        for eval_id, attempt in self.__latest_graded_attempts(enrollment).items():
            eval = self.evaluation_repository.find_by_id(eval_id)
            if eval.module_id in module_grades:
                previous_grade = module_grades[eval.module_id]
                module_grades[eval.module_id] = round(attempt.grade * eval.weight + previous_grade * (1 - eval.weight), 2)
            else:
                module_grades[eval.module_id] = attempt.grade

        return module_grades

    
    def calculate_student_average(self, enrollment: Enrollment) -> float:

        return round(statistics.mean(self.grades_for_modules(enrollment).values()), 2)

    def get_grade_for_module(self, enrollment: Enrollment, module: Module):
        return self.grades_for_modules(enrollment=enrollment).get(module.id)
    
    def get_grade_color(self, grade: float, target: float|None = None) -> str:
        if not target:
            target = self.DEFAULT_TARGET

        if grade < target - self.DEVIATION:
            return "grade-green"
        if grade > target + self.DEVIATION:
            return "grade-red"
        return "grade-yellow"