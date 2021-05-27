# TimeKeeper-Back-End
Django and Django REST Framework Back-End designed for the TimeKeeper Web App.

TimeKeeper-Back-End handles API requests from TimeKeeper-Front-End (https://github.com/Arivald8/TimeKeeper-Front-End).
It also allows to render test Views using Django REST Generics.

---

### Currently it's possible to filter results in the following ways:
- All objects. [base url domain] e.g. **localhost:8000**
  ![All objects](https://i.ibb.co/PwXqKVv/all-view.jpg)
- Single object. [domain + id] e.g. **localhost:8000/1/**
  ![Single object](https://i.ibb.co/Bj8wZFt/single-view.jpg)
- All objects matching a given date. [domain + date] e.g. **localhost:8000/2021-05-20/**
  ![All objects with date x](https://i.ibb.co/fQLHLsP/date-view.jpg)
- All objects within a weekly range of dates. End of range is always the upcoming Monday. [domain + /weekly/ + date] e.g. **localhost:8000/weekly/2021-05-19/**

  ![All objects within a range](https://i.ibb.co/kcKJ5WJ/date-range-view.jpg)

---

### It's also possible to create and update:
- Create a test activity [domain + /create/] e.g. **localhost:8000/create/**
  ![Create activity](https://i.ibb.co/Ry371sC/create-view.jpg)
- Update an activity [domain + /update/pk/activity_date] e.g. **localhost:8000/update/1/2021-05-19/**
  ![Update activity](https://i.ibb.co/Dt71gmH/update-view.jpg)
