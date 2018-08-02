class Dispatcher:

    def startElement(self, name, attrs):
        self.dispatch('start', name, attrs)

    def endElement(self, name):
        self.dispatch('end', name)

    def dispatch(self, prefix, name, attrs=None):
        mname = prefix + name.capitalize()
        dname = 'default ' + prefix.capitalize()
        method = getattr(self, mname, None)
        if callable(method):
            args = ()
        else:
            method = getattr(self, dname, None)
            args = name
        if prefix == 'start':
            args += attrs,
        if callable(method):
            method(*args)

