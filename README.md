# Фреймворк для автоматизации тестирования API [Vikunja](https://vikunja.io/) 
<img align="center" src="https://github.com/Lexzender/vikunja_api_test_framework/blob/main/vikunja_api_test_framework/pictures/vikunja.png" />

---

## Особенности проекта
* Автоматизация отчетности о тестовых прогонах и тест-кейсах в Jira
* Интеграция с Allure TestOps
* Отчеты Allure Report
* Сборка проекта в Jenkins
* Отчеты с request body, response body, status code
* Оповещения о тестовых прогонах в Telegram
* Валидация типов данных
---
## Список проверок, реализованных в проекте
* Авторизация
* Успешная регистрация пользователя
* Неуспешная регистрация пользователя 
* Создание нового проекта
* Получение проекта по id
* Удаление проекта

 ---
## Запуск проекта
Запустить проект можно локально по команде

```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest -s -v 
```
Или в Jenkins

### <code><img width="3%" title="Jenkins" src="https://github.com/Lexzender/Lexzender/blob/main/images/jenkins-original.svg"></code> Запуск проекта в Jenkins

1) Открыть [проект](https://jenkins.autotests.cloud/job/vikunja_api_test_framework/)
2) Нажать "Build with Parameters"
3) Заполнить параметры 
4) Нажать "Build"
<img align="center" src="https://github.com/Lexzender/vikunja_api_test_framework/blob/main/vikunja_api_test_framework/pictures/jenkins_api.png" />

---

## <code><img width="3%" title="Allure_Report" src="https://github.com/Lexzender/Lexzender/blob/main/images/Allure_Report.png"></code> Allure report
### После прохождения тестов результаты можно посмотреть в Allure отчете
<img align="center" src="https://github.com/Lexzender/vikunja_api_test_framework/blob/main/vikunja_api_test_framework/pictures/allure_api.png" />

### В отчете для каждого теста указана мета информация, а также приложены результаты прохождения: отчеты с request body, response body, status code.
<img align="center" src="https://github.com/Lexzender/vikunja_api_test_framework/blob/main/vikunja_api_test_framework/pictures/behaaviors_api.png" />

---
## <code><img width="3%" title="AllureTestOps.png" src="https://github.com/Lexzender/Lexzender/blob/main/images/AllureTestOps.png"></code> Интеграция с Allure TestOps
### Тест кейсы
<img align="center" src="https://github.com/Lexzender/vikunja_api_test_framework/blob/main/vikunja_api_test_framework/pictures/test%20%20cases_api.png" />

### Тестовые артефакты 
<img align="center" src="https://github.com/Lexzender/vikunja_api_test_framework/blob/main/vikunja_api_test_framework/pictures/tk_api.png" />

---
## <code><img width="3%" title="Jira.png" src="https://github.com/Lexzender/Lexzender/blob/main/images/jira-original.svg"></code> Интеграция с Jira
<img align="center" src="https://github.com/Lexzender/vikunja_api_test_framework/blob/main/vikunja_api_test_framework/pictures/jira_api.png" />

---
## <code><img width="3%" title="Telegram" src="https://github.com/Lexzender/Lexzender/blob/main/images/tg.png"></code> Нотификация в Telegram
После прохождения тестов результаты будут отправлены в Telegram
<img align="center" src="https://github.com/Lexzender/vikunja_api_test_framework/blob/main/vikunja_api_test_framework/pictures/Telegram_api.png" />

