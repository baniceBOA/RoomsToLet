# UTILITY


# search Controller

from controller import AccountController, HouseController, RoomController, LandlordController


def searchController(query=''):
	''' Search the query from the entire tables in the database '''
	result = dict()
	controllers = [AccountController(),HouseController(), RoomController(), LandlordController() ]
	for controller in controllers:
		result[controller.name] = controller.query(query)

	return result