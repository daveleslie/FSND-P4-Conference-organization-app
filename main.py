#!/usr/bin/env python

"""
main.py -- Udacity conference server-side Python App Engine
    HTTP controller handlers for memcache & task queue access

$Id$

created by wesc on 2014 may 24

"""

__author__ = 'wesc+api@google.com (Wesley Chun)'

import webapp2
from google.appengine.api import app_identity
from google.appengine.api import mail
from google.appengine.api import memcache
from conference import ConferenceApi

class SetAnnouncementHandler(webapp2.RequestHandler):
    def get(self):
        """Set Announcement in Memcache."""
        # TODO 1
        # use _cacheAnnouncement() to set announcement in Memcache
        ConferenceApi._cacheAnnouncement()


class SendConfirmationEmailHandler(webapp2.RequestHandler):
    def post(self):
        """Send email confirming Conference creation."""
        mail.send_mail(
            'noreply@%s.appspotmail.com' % (
                app_identity.get_application_id()),     # from
            self.request.get('email'),                  # to
            'You created a new Conference!',            # subj
            'Hi, you have created the following '         # body
            'conference:\r\n\r\n%s' % self.request.get(
                'conferenceInfo')
        )


class setFeaturedSpeakerHandler(webapp2.RequestHandler):
    def post(self):
        """Set featured speaker in memcache"""
        websafeKey = self.request.get('websafeKey')
        speaker = self.request.get('speaker')

        sessions = ConferenceApi._getSessionsBySpeaker(websafeKey, speaker)
        if sessions.count() > 1:
            featuredSpeakerNotice = "%s is a featured speaker for %s sessions" \
                              % (speaker, sessions.count())
            memcache.set(websafeKey, featuredSpeakerNotice)

app = webapp2.WSGIApplication([
    ('/crons/set_announcement', SetAnnouncementHandler),
    ('/tasks/send_confirmation_email', SendConfirmationEmailHandler),
    ('/tasks/featured_speaker', setFeaturedSpeakerHandler),
], debug=True)
