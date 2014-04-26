def set_system_encoding_utf8():
    import sys
    reload(sys)
    sys.setdefaultencoding("utf-8")
