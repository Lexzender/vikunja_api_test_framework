# Фреймворк для автоматизации тестирования API Petstore
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
### Запуск проекта в Jenkins

1) Открыть [проект](https://jenkins.autotests.cloud/job/luma_UI_test_framework/)
2) Нажать "Build with Parameters"
3) Заполнить параметры 
4) Нажать "Build"
<img align="center" src="https://github.com/Lexzender/luma_UI_test_framework/blob/main/luma_UI_test_framework/pictures/jenkins.png" />

---

## Allure report
### После прохождения тестов, результаты можно посмотреть в Allure отчете
