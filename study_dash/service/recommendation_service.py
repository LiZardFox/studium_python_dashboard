from .service import Service, ServiceContainer
from study_dash.entity import Enrollment
from study_dash.repository import ModuleRepository


class RecommendationService(Service):
    """
    Service class for next module finish recommendation calculation.
    Extends the Service class.
    """

    def __init__(self, service_container: ServiceContainer):
        self.module_repository = service_container.get_service(ModuleRepository)


    def calculate_recommended_end(self, enrollment: Enrollment, target = bool):
        all_modules = self.module_repository.find_many_by_sql(
            'SELECT DISTINCT mo.*'
            ' FROM module mo'
            ' INNER JOIN program_module pm ON mo.id = pm.module_id'
            ' WHERE pm.program_id = ?'
            ' ORDER BY pm.sort',
            (enrollment.program_id,)
        )
        passed_modules = self.module_repository.find_many_by_sql(
                    'SELECT DISTINCT mo.*'
                    ' FROM module mo'
                    ' INNER JOIN evaluation ev ON mo.id = ev.module_id'
                    ' INNER JOIN attempt at ON ev.id = at.evaluation_id'
                    ' INNER JOIN program_module pm ON mo.id = pm.module_id'
                    ' WHERE pm.program_id = ?'
                    ' AND at.enrollment_id = ?'
                    ' AND (at.grade IS NOT NULL AND at.grade < 5)'
                    ' ORDER BY pm.sort',
                    (enrollment.program_id, enrollment.id)
                )
        end_date = enrollment.target_end_date if target else enrollment.end_date 
        time_per_module = (end_date - enrollment.start_date) / len(all_modules)
        recommended_end = enrollment.start_date + len(passed_modules) * time_per_module + time_per_module
        return recommended_end

