
class ObjectUtils:

    @staticmethod
    def exists(obj) -> bool:
        try:
            obj
        except NameError:
            return False
        finally:
            return True