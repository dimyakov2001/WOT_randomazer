from abc import ABCMeta


class GUIObject:
    __metaclass__ = ABCMeta

    GUI_OBJECT_COMMAND_FIELD = "command"
    GUI_OBJECT_STATE_FIELD = "state"
    GUI_OBJECT_STATE_DISABLED = "disabled"
    GUI_OBJECT_STATE_ENABLED = "active"
    GUI_OBJECT_TEXT_FIELD = "text"

    _object = None

    def __getitem__(self, item):
        return self._object[item]

    def __setitem__(self, key, value):
        self._object[key] = value

    def locate(self, location_dict):
        self._object.grid(location_dict)

    def keys(self):
        return self._object.keys()

    def _create_object_by_type(self, object_type, master_object):
        if isinstance(master_object, GUIObject):
            self._object = object_type(master_object._object)
        else:
            self._object = object_type()

    def _set_properties_to_object(self, properties_dict):
        for property_to_set in properties_dict.keys():
            self._object[property_to_set] = properties_dict[property_to_set]
