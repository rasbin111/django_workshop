from rest_framework.throttling import  UserRateThrottle

class CourseListThrottling(UserRateThrottle):
    scope = "course-list"