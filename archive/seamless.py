import sys
import sublime, sublime_plugin
import pickle as xml_pickle
import json
import inspect
import thread
import SeamlessClient as client
from time import sleep



class SeamlessCommand(sublime_plugin.EventListener):
        
        Send_data = 0
        Recv_data = 0

        def on_load(self, view):                
                print 'thread runnin'
                print self.Recv_data, 'printing'
                thread.start_new_thread(self.update, (view,''))

                chat = client('butteryseamless@gmail.com', 'OlinCollege')
                chat.use_signals(signals=['SIGHUP','SIGTERM','SIGINT'])
                chat.connect()
                chat.process(block=False)
                chat.send("test")
			
				
                
        def on_modified(self, view):

                reg = sublime.Region(0, 10000)
                self.Send_data = str(view.substr(reg))
                print self.Send_data
                #print view.sel()
                print "onmod recv", self.Recv_data
                self.update(view, '')

        def on_post_save(self, view):
                #print "on_save called"
                self.Recv_data = "apples"
                print self.Recv_data


        def update(self, view, string):
                print "recv", self.Recv_data
                while(self.Recv_data != 0):
                        edit = view.begin_edit()
                        view.insert(edit, 0, self.Recv_data)
                        self.Recv_data = 0

