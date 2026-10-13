from django.utils import timezone

from tracker.models import Application, Company, ProfileSkill, Reminder, Skill, StudentProfile, Vacancy
from tracker.services import ensure_skill_catalog

DEMO_SOURCE = 'demo'

DEMO_VACANCIES = [
    ("SoftServe", "Python Internship", ['python', 'sql', 'rest'], "Київ", 400, 600, "https://career.softserveinc.com"),
    ("EPAM", "QA Trainee", ['qa', 'sql', 'postman'], "Львів", 300, 450, "https://training.epam.ua"),
    ("Genesis", "Backend Trainee", ['python', 'sql', 'rest', 'docker'], "Київ", 500, 700, "https://gen.tech"),
    ("Ajax Systems", "Junior QA / Python Engineer", ['python', 'linux', 'pytest'], "Київ", 700, 900, "https://ajax.systems"),
    ("GlobalLogic", "Python BaseCamp", ['python', 'git', 'linux'], "Віддалено", None, None, "https://globallogic.com"),
    ("Luxoft", "Java Intern", ['java', 'spring', 'sql'], "Дніпро", 350, 500, "https://career.luxoft.com"),
    ("Intellias", "Frontend Trainee", ['javascript', 'html', 'css', 'react'], "Львів", 300, 480, "https://intellias.com"),
    ("Grammarly", "Data Science Intern", ['python', 'pandas', 'machine learning'], "Віддалено", 800, 1100, "https://grammarly.com"),
]

DEMO_APPLICATIONS = [
    (0, 'applied', 2, [(2, "Технічна співбесіда з техлідом (MS Teams)", False)]),
    (1, 'applied', 14, [(-3, "Очікую результатів вступного тесту з англійської", False)]),
    (2, 'applied', 4, [(1, "HR-скринінг дзвінок на 30 хвилин", False)]),
    (3, 'offer', 22, [(5, "Уточнити в рекрутера деталі та наступні кроки", False)]),
    (4, 'found', 45, [(12, "Дедлайн подачі анкети", False)]),
    (5, 'rejected', 30, [(-10, "Відповідь від рекрутера", True)]),
]
