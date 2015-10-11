import sublime
import sublime_plugin
import os
import functools

class FileDeleteCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        filename = self.view.file_name()

        if not os.access(filename, os.W_OK):
            sublime.error_message(leaf + " is read-only")

        try:
            os.remove(filename)
        except Exception as e:
            sublime.status_message("Unable to delete: " + str(e))


