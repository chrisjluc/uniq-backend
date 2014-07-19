from rest_framework.exceptions import APIException

class CouldNotBeFoundException(APIException):
	status_code=404
	default_detail="Doesn't exist"