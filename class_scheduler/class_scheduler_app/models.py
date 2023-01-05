from django.db import models

# Create your models here.
class Course(object):
    def __init__(self, id_param, title_param, description_param,
                 units_param, prereq_param, lecture_sections_param,
                 lab_sections_param, quiz_sections_param, discussion_sections_param):
        """Constructs a new Course object
        Parameters: 9
        id: id of the course (PublishedCourseID) such as CSCI-103 (String)
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
    def prereq(self):
        return self._prereq

    @property
    def lecture_sections(self):
        return self._lecture_sections

    @property
    def lab_sections(self):
        return self._lab_sections

    @property
    def quiz_sections(self):
        return self._quiz_sections

    @property
    def discussion_sections(self):
        return self._discussion_sections
    
    @id.setter
    def id(self, new_id):
        self._id = new_id
        
    @title.setter
    def title(self, new_title):
        self._title = new_title
        
    @description.setter
    def description(self, new_description):
        self._description = new_description
        
    @units.setter
    def unit(self, new_units):
        self._units = new_units
    
    @prereq.setter
    def prereq(self, new_prereq):
        self._prereq.append(new_prereq)

    @lecture_sections.setter
    def lecture_sections(self, new_lecture_section):
        self._lecture_sections.append(new_lecture_section)

    @lab_sections.setter
    def lab_sections(self, new_lab_sections):
        self._lab_sections.append(new_lab_sections)

    @quiz_sections.setter
    def quiz_sections(self, new_quiz_sections):
        self._quiz_sections.append(new_quiz_sections)

    @discussion_sections.setter
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
        end_time: time section ends in military time (ex: "13:50") (string)
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
    
    @id.setter
    def id(self, new_id):
        self._id = new_id
        
    @clearance_code.setter
    def clearance_code(self, new_clearance_code):
        self._clearance_code = new_clearance_code
    
    @type.setter
    def type(self, new_type):
        self._type = new_type
        
    @spaces_available.setter
    def spaces_available(self, new_spaces):
        self._spaces_available = new_spaces
        
    @day.setter
    def day(self, new_day):
        self._day = new_day
        
    @start_time.setter
    def start_time(self, new_start_time):
        self._start_time = new_start_time
        
    @end_time.setter
    def end_time(self, new_end_time):
        self._end_time = new_end_time
        
    @location.setter
    def location(self, new_location):
        self._location = new_location

# dummy data to be used for initial backtracking
# based on Huong's Spring 2023 schedule

chem105_lecture1 = Section(1, "R", "Lec", 5, "MWF", "9:00", "9:50", "zoom")
chem105_lecture2 = Section(2, "R", "Lec", 5, "TTH", "10:00", "10:50", "zoom")
chem105_lab = Section(3, "R", "Lab", 5, "TH", "11:00", "13:50", "zoom")
chem105_quiz = Section(4, "R", "Qz", 5, "T", "15:30", "16:50", "zoom")
chem105 = Course("CHEM-105A", "Intro to Chemistry", "description", 4, "",
                 [chem105_lecture1, chem105_lecture2], [chem105_lab], [chem105_quiz], [])

psych100_lecture1 = Section(11, "R", "Lec", 5, "TTH", "9:30", "10:50", "zoom")
psych100_lecture2 = Section(22, "R", "Lec", 5, "MW", "8:00", "8:50", "zoom")
psych100_lab = Section(33, "R", "Lab", 5, "T", "12:00", "13:50", "zoom")
psych100 = Course("PSYCH-100", "Intro to Psychology", "description", 4, "", [psych100_lecture1, psych100_lecture2], [psych100_lab], [], [])

csci360_lecture1 = Section(111, "D", "Lec", 5, "MW", "12:00", "13:50", "zoom")
csci360 = Course("CSCI-360", "Intro to Artificial Intelligence", "description", 4, "", [csci360_lecture1], [], [], [])

csci350_lecture1 = Section(1111, "D", "Lec", 5, "F", "12:00", "15:20", "SAL101")
csci350 = Course("CSCI-350", "Intro to Operating Systems", "description", 4, "", [csci350_lecture1], [], [], [])

itp125_lecture1 = Section(11111, "R", "Lec", 5, "M", "18:00", "19:50", "zoom")
itp125 = Course("ITP-125", "From Hackers to CEO: Intro to Information Security", "description", 2, "", 
                [itp125_lecture1], [], [], [])


# print(chem105)
# print(psych100)
# print(csci360)
# print(csci350)
# print(itp125)



