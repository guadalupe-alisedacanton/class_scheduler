from django.db import models

# Create your models here.
class Course(object):
    def __init__(self, id_param, title_param, description_param,
                 units_param, prereq_param, lecture_sections_param,
                 lab_sections_param, quiz_sections_param, discussion_sections_param):
        """Constructs a new Course object
        Parameters: 9
        id: id of the course such as 103 (int)
        title: title of the course such Introduction to Programming (string)
        description: description of the course (string)
        units: number of units for the course such as 2 or 4 units (int)
        prereq: the prerequisite classes for this course (list of ints (class ids))
        sections: section objects such as lectures, labs, quizzes, etc (list of objects)"""
        self._id = id_param
        self._title = title_param
        self._description = description_param
        self._units = units_param
        self._prereq = prereq_param
        self._lecture_sections = lecture_sections_param
        self._lab_sections = lab_sections_param
        self._quiz_sections = quiz_sections_param
        self._discussion_sections = discussion_sections_param


    @property
    def id(self):
        return self._id

    @property
    def title(self):
        return self._title

    @property
    def description(self):
        return self._description

    @property
    def units(self):
        return self._units

    @property
    def get_prereq(self):
        return self._prereq

    @property
    def lecture_sections(self):
        return self._lecture_sections

    @property
    def _lab_sections(self):
        return self._lab_sections

    @property
    def _quiz_sections(self):
        return self._quiz_sections

    @property
    def discussion_sections(self):
        return self._discussion_sections

    @lecture_sections.setter
    def lecture_sections(self, new_lecture_section):
        self._lecture_sections.append(new_lecture_section)

    @_lab_sections.setter
    def _lab_sections(self, new_lab_sections):
        self._lab_sections.append(new_lab_sections)

    @_quiz_sections.setter
    def _quiz_sections(self, new_quiz_sections):
        self._quiz_sections.append(new_quiz_sections)

    @discussion_sections
    def discussion_sections(self, new_discussion_sections):
        self._discussion_sections.append(new_discussion_sections)
        
        
class Section(object):
    def __init__(self, id, clearance_code, type,
                 spaces_available, day, start_time,
                 end_time, location):
        """
        Constructs a new Section object
        Parameters: 8
        id: id of the section (int)
        clearance code: either R or D (string)
        type: Lec, Lab, Dis, or Qz (string)
        spaces_avaiable: number of spots left (int)
        day: day the section meets (M, T, W, TH or F) (string)
        start_time: time section starts in military time (ex: "12:30") (string)
        start_time: time section ends in military time (ex: "13:50") (string)
        location: the room the section meets at (string)
        """
        self._id = id
        self._clearance_code = clearance_code
        self._type = type
        self._spaces_available = spaces_available
        self._day = day
        self._start_time = start_time
        self._end_time = end_time
        self._location = location


    @property
    def id(self):
        return self._id

    @property
    def clearance_code(self):
        return self._clearance_code

    @property
    def type(self):
        return self._type

    @property
    def spaces_available(self):
        return self._spaces_available

    @property
    def day(self):
        return self._day

    @property
    def start_time(self):
        return self._start_time

    @property
    def end_time(self):
        return self._end_time

    @property
    def location(self):
        return self._location