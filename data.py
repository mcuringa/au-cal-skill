from datetime import date

fall = {
  "summer-graduation": {
    "key": "summer-graduation",
    "event": "Official Summer Graduation Date",
    "start": date.fromiso("2020-08-31"),
    "end": None,
    "no-school": False
  },
  "first-day-fall": {
    "key": "first-day-fall",
    "event": "First Day of Classes",
    "start": date.fromiso("2020-08-31"),
    "end": None,
    "no-school": False
  },
  "labor-day": {
    "key": "labor-day",
    "event": "Labor Day Weekend - No Classes",
    "start": date.fromiso("2020-09-05"),
    "end": date.fromiso("2020-09-07"),
    "no-school": True
  },
  "last-day-add": {
    "key": "last-day-add",
    "event": "Last Day to Add a Course",
    "start": date.fromiso("2020-09-14"),
    "end": None,
    "no-school": False
  },
  "last-day-section": {
    "key": "last-day-section",
    "event": "Last Day to Process Course Section Change",
    "start": date.fromiso("2020-09-28"),
    "end": None,
    "no-school": False
  },
  "last-day-ind-study": {
    "key": "last-day-ind-study",
    "event": "Last Day to Add Independent Study or Internship",
    "start": date.fromiso("2020-09-28"),
    "end": None,
    "no-school": False
  },
  "last-day-grading": {
    "key": "last-day-grading",
    "event": "Last Day to Change a Course Grading Option",
    "start": date.fromiso("2020-09-28"),
    "end": None,
    "no-school": False
  },
  "last-day-drop": {
    "key": "last-day-drop",
    "event": "Last Day to Drop a Course",
    "start": date.fromiso("2020-09-28"),
    "end": None,
    "no-school": False
  },
  "open-planning": {
    "key": "open-planning",
    "event": "Open Planning Begins for Spring 2021",
    "start": date.fromiso("2020-10-26"),
    "end": None,
    "no-school": False
  },
  "last-day-withdraw": {
    "key": "last-day-withdraw",
    "event": "Last Day to Withdraw",
    "start": date.fromiso("2020-11-02"),
    "end": None,
    "no-school": False
  },
  "election-day": {
    "key": "election-day",
    "event": "Election Day - No Classes",
    "start": date.fromiso("2020-11-03"),
    "end": None,
    "no-school": True
  },
  "grad-registration": {
    "key": "grad-registration",
    "event": "Graduate Registration begins for Spring 21",
    "start": date.fromiso("2020-11-11"),
    "end": None,
    "no-school": False
  },
  "undergrad-registration": {
    "key": "undergrad-registration",
    "event": "Undergraduate Registration begins for Spring 21",
    "start": date.fromiso("2020-11-13"),
    "end": None,
    "no-school": False
  },
  "last-day-in-person": {
    "key": "last-day-in-person",
    "event": "Last day of in-person instruction",
    "start": date.fromiso("2020-11-24"),
    "end": None,
    "no-school": False
  },
  "thanksgiving-break": {
    "key": "thanksgiving-break",
    "event": "Thanksgiving Break - No Classes",
    "start": date.fromiso("2020-11-25"),
    "end": date.fromiso("2020-11-29"),
    "no-school": True
  },
  "res-halls-close": {
    "key": "res-halls-close",
    "event": "Residence halls closed for the fall semester",
    "start": date.fromiso("2020-11-25"),
    "end": None,
    "no-school": False
  },
  "makeup-day": {
    "key": "makeup-day",
    "event": "MakeUp/Study Day",
    "start": date.fromiso("2020-12-14"),
    "end": None,
    "no-school": False
  },
  "finals-week": {
    "key": "finals-week",
    "event": "Online/remote final exam period",
    "start": date.fromiso("2020-12-15"),
    "end": date.fromiso("2020-12-21"),
    "no-school": False
  }
}

spring = {
  "first-day-winter": {
    "key": "first-day-winter",
    "event": "First Day of Classes - Intersession ",
    "start": date.fromiso("2020-01-04"),
    "end": None,
    "no-school": False
  },
  "mlk": {
    "key": "mlk",
    "event": "Martin Luther King Jr Birthday - No Classes ",
    "start": date.fromiso("2020-01-18"),
    "end": None,
    "no-school": True
  },
  "last-day-winter": {
    "key": "last-day-winter",
    "event": "Last Day of Classes - Intersession ",
    "start": date.fromiso("2020-01-22"),
    "end": None,
    "no-school": False
  },
  "first-day-spring": {
    "key": "first-day-spring",
    "event": "First Day of Classes - Spring ",
    "start": date.fromiso("2020-01-26"),
    "end": None,
    "no-school": False
  },
  "last-day-add": {
    "key": "last-day-add",
    "event": "Last Day to Add a Course ",
    "start": date.fromiso("2020-02-08"),
    "end": None,
    "no-school": False
  },
  "last-day-ind-study": {
    "key": "last-day-ind-study",
    "event": "Last Day to Add an Independent Study or Internship ",
    "start": date.fromiso("2020-02-23"),
    "end": None,
    "no-school": False
  },
  "last-day-drop": {
    "key": "last-day-drop",
    "event": "Last Day to Drop a Course ",
    "start": date.fromiso("2020-02-23"),
    "end": None,
    "no-school": False
  },
  "last-day-grading": {
    "key": "last-day-grading",
    "event": "Last Day to Change a Course Grading Option ",
    "start": date.fromiso("2020-02-23"),
    "end": None,
    "no-school": False
  },
  "last-day-section": {
    "key": "last-day-section",
    "event": "Last Day to Process Course Section Change ",
    "start": date.fromiso("2020-02-23"),
    "end": None,
    "no-school": False
  },
  "open-planning": {
    "key": "open-planning",
    "event": "First Day of Open Planning for Sum and Fall 2021 ",
    "start": date.fromiso("2020-03-08"),
    "end": None,
    "no-school": False
  },
  "mini1": {
    "key": "mini1",
    "event": "No Classes, Spring Mini-Break ",
    "start": date.fromiso("2020-03-10"),
    "end": None,
    "no-school": True
  },
  "mini2": {
    "key": "mini2",
    "event": "No Classes, Spring Mini-Break ",
    "start": date.fromiso("2020-03-20"),
    "end": None,
    "no-school": True
  },
  "mini3": {
    "key": "mini3",
    "event": "No Classes, Spring Mini-Break ",
    "start": date.fromiso("2020-03-21"),
    "end": None,
    "no-school": True
  },
  "Summer-registration": {
    "key": "Summer-registration",
    "event": "Registration begins for Summer 21 ",
    "start": date.fromiso("2020-03-22"),
    "end": None,
    "no-school": False
  },
  "last-day-withdraw": {
    "key": "last-day-withdraw",
    "event": "Last Day to Withdraw ",
    "start": date.fromiso("2020-03-30"),
    "end": None,
    "no-school": False
  },
  "grad-registration": {
    "key": "grad-registration",
    "event": "Graduate registration begins for Fall 21 ",
    "start": date.fromiso("2020-03-31"),
    "end": None,
    "no-school": False
  },
  "mini4": {
    "key": "mini4",
    "event": "No Classes, Spring Mini-Break ",
    "start": date.fromiso("2020-04-01"),
    "end": None,
    "no-school": True
  },
  "undergrad-registration": {
    "key": "undergrad-registration",
    "event": "Undergraduate registration begins for Fall 21 ",
    "start": date.fromiso("2020-04-05"),
    "end": None,
    "no-school": False
  },
  "mini5": {
    "key": "mini5",
    "event": "No Classes, Spring Mini-Break ",
    "start": date.fromiso("2020-04-16"),
    "end": None,
    "no-school": True
  },
  "research-day": {
    "key": "research-day",
    "event": "Research and Creative Works Conference - No Classes ",
    "start": date.fromiso("2020-04-27"),
    "end": None,
    "no-school": True
  },
  "mini6": {
    "key": "mini6",
    "event": "No Classes, Spring Mini-Break ",
    "start": date.fromiso("2020-05-03"),
    "end": None,
    "no-school": True
  },
  "makeup1": {
    "key": "makeup1",
    "event": "Makeup/Study Day - No classes ",
    "start": date.fromiso("2020-05-11"),
    "end": None,
    "no-school": True
  },
  "makeup2": {
    "key": "makeup2",
    "event": "Makeup/Study Day - No classes ",
    "start": date.fromiso("2020-05-12"),
    "end": None,
    "no-school": True
  },
  "makeup3": {
    "key": "makeup3",
    "event": "Makeup/Study Day - No classes ",
    "start": date.fromiso("2020-05-13"),
    "end": None,
    "no-school": True
  },
  "finals-week": {
    "key": "finals-week",
    "event": "Final Exam period ",
    "start": date.fromiso("2020-05-14"),
    "end": date.fromiso("2020-05-20"),
    "no-school": False
  },
  "doc-hooding": {
    "key": "doc-hooding",
    "event": "Doctoral Hooding ",
    "start": date.fromiso("2020-05-21"),
    "end": None,
    "no-school": False
  },
  "graduation": {
    "key": "graduation",
    "event": "Commencement Ceremony ",
    "start": date.fromiso("2020-05-24"),
    "end": None,
    "no-school": False
  }
}
