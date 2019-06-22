from django.conf.urls import url, include
from django.urls import path
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view

from . import views, view_utils, data_utils, table_utils
from . import api_views
from .form_views import *

schema_view = get_schema_view(title='Young Supernova Experiment (YSE) API')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
	# ex: /yse/
    url(r'^$', views.index, name='index'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^personaldashboard/$', views.personaldashboard, name='personaldashboard'),
    url(r'^calendar/$', views.calendar, name='calendar'),
    url(r'^followup/$', views.followup, name='followup'),
	url(r'^transient_tags/$', views.transient_tags, name='transient_tags'),
	url(r'^get_transient_tags/$', views.get_transient_tags, name='get_transient_tags'),

    url(r'^dashboard_example/$', views.dashboard_example, name='dashboard_example'),
    url(r'^transient_edit/$', views.transient_edit, name='transient_edit'),
    url(r'^transient_edit/(?P<transient_id>[0-9]+)/$', views.transient_edit, name='transient_edit'),
    url(r'^transient_detail/(?P<slug>[a-zA-Z0-9_-]+)/$', views.transient_detail, name='transient_detail'),

    url(r'^observing_calendar/$', views.observing_calendar, name='observing_calendar'),
    url(r'^observing_night/(?P<telescope>.*)/(?P<obs_date>[a-zA-Z0-9_-]+)/$', views.observing_night, name='observing_night'),

	url(r'^get_transient/(?P<slug>[a-zA-Z0-9_-]+)/$', data_utils.get_transient, name='get_transient'),
	url(r'^add_transient/', data_utils.add_transient, name='add_transient'),
	url(r'^add_gw_candidate/', data_utils.add_gw_candidate, name='add_gw_candidate'),
	url(r'^add_transient_phot/', data_utils.add_transient_phot, name='add_transient_phot'),
	url(r'^add_transient_spec/', data_utils.add_transient_spec, name='add_transient_spec'),
	url(r'^get_host/(?P<ra>\d+\.\d+)/(?P<dec>[+-]?\d+\.\d+)/(?P<sep>\d+\.?\d*)/$', data_utils.get_host, name='get_host'),
	url(r'^download_data/(?P<slug>[a-zA-Z0-9_-]+)/$', views.download_data, name='download_data'),
	url(r'^download_photometry/(?P<slug>[a-zA-Z0-9_-]+)/$', views.download_photometry, name='download_photometry'),
	url(r'^download_target_list/(?P<telescope>[a-zA-Z0-9_-]+)/(?P<obs_date>[a-zA-Z0-9_-]+)/$', views.download_target_list, name='download_target_list'),
	url(r'^download_targets_and_finders/(?P<telescope>[a-zA-Z0-9_-]+)/(?P<obs_date>[a-zA-Z0-9_-]+)/$', views.download_targets_and_finders, name='download_targets_and_finders'),
	url(r'^upload_spectrum/', views.upload_spectrum, name='upload_spectrum'),
	
    url(r'^login/$', views.auth_login, name='auth_login'),
    url(r'^logout/$', views.auth_logout, name='auth_logout'),
    url(r"^airmassplot/(?P<transient_id>[0-9]+)/(?P<obs_id>[a-zA-Z0-9_-]+)/(?P<telescope_id>[a-zA-Z0-9]+)", 
		view_utils.airmassplot, name='airmassplot'),
    url(r'^lightcurveplot/(?P<transient_id>[0-9]+)/$', view_utils.lightcurveplot, name='lightcurveplot'),
    url(r'^salt2plot/(?P<transient_id>[0-9]+)/(?P<salt2fit>[0-1]+)/$', view_utils.salt2plot, name='salt2plot'),
    url(r'^spectrumplot/(?P<transient_id>[0-9]+)/$', view_utils.spectrumplot, name='spectrumplot'),
    url(r'^spectrumplotsingle/(?P<transient_id>[a-zA-Z0-9_-]+)/(?P<spec_id>[a-zA-Z0-9_-]+)/$', view_utils.spectrumplotsingle, name='spectrumplotsingle'),
	url(r'^finderchart/(?P<transient_id>[0-9]+)/$', view_utils.finder().finderchart, name='finderchart'),
	url(r'^finderim/(?P<transient_id>[0-9]+)/$', view_utils.finder().finderim, name='finderim'),
	
	url(r'^add_transient_followup/', AddTransientFollowupFormView.as_view(), name='add_transient_followup'),
    url(r'^add_transient_observation_task/', AddTransientObservationTaskFormView.as_view(), name='add_transient_observation_task'),
    url(r'^add_transient_comment/', AddTransientCommentFormView.as_view(), name='add_transient_comment'),
	url(r'^add_dashboard_query/', AddDashboardQueryFormView.as_view(), name='add_dashboard_query'),
	url(r'^remove_dashboard_query/(?P<pk>[0-9_-]+)/', RemoveDashboardQueryFormView.as_view(), name='remove_dashboard_query'),
	url(r'^rise_time/(?P<transient_id>[0-9]+)/(?P<obs_id>[a-zA-Z0-9_-]+)',
		view_utils.rise_time, name='rise_time'),
	url(r'^set_time/(?P<transient_id>[0-9]+)/(?P<obs_id>[a-zA-Z0-9_-]+)',
		view_utils.set_time, name='set_time'),
	url(r'^moon_angle/(?P<transient_id>[0-9]+)/(?P<obs_id>[a-zA-Z0-9_-]+)',
		view_utils.moon_angle, name='moon_angle'),
	url(r'^tonight_rise_time/(?P<transient_id>[0-9]+)/(?P<too_id>[a-zA-Z0-9_-]+)',
		view_utils.tonight_rise_time, name='tonight_rise_time'),
	url(r'^tonight_set_time/(?P<transient_id>[0-9]+)/(?P<too_id>[a-zA-Z0-9_-]+)',
		view_utils.tonight_set_time, name='tonight_set_time'),
	url(r'^tonight_moon_angle/(?P<transient_id>[0-9]+)/(?P<too_id>[a-zA-Z0-9_-]+)',
		view_utils.tonight_moon_angle, name='tonight_moon_angle'),

	url(r'^delta_too_hours/(?P<transient_id>[0-9]+)/(?P<too_id>[a-zA-Z0-9_-]+)',
		view_utils.delta_too_hours, name='delta_too_hours'),

	url(r'^get_ps1_image/(?P<transient_id>[0-9]+)',
		view_utils.get_ps1_image, name='get_ps1_image'),
	url(r'^get_hst_image/(?P<transient_id>[0-9]+)',
		view_utils.get_hst_image, name='get_hst_image'),
	url(r'^get_chandra_image/(?P<transient_id>[0-9]+)',
		view_utils.get_chandra_image, name='get_chandra_image'),
	url(r'^get_legacy_image/(?P<transient_id>[0-9]+)',
		view_utils.get_legacy_image, name='get_legacy_image'),

    path('accounts/', include('django.contrib.auth.urls')),
	url(r'^explorer/', include('explorer.urls')),
]

router = DefaultRouter()
router.register(r'transientwebresources', api_views.TransientWebResourceViewSet)
router.register(r'hostwebresources', api_views.HostWebResourceViewSet)
router.register(r'transientstatuses', api_views.TransientStatusViewSet)
router.register(r'followupstatuses', api_views.FollowupStatusViewSet)
router.register(r'taskstatuses', api_views.TaskStatusViewSet)
router.register(r'antaresclassifications', api_views.AntaresClassificationViewSet)
router.register(r'internalsurveys', api_views.InternalSurveyViewSet)
router.register(r'observationgroups', api_views.ObservationGroupViewSet)
router.register(r'sedtypes', api_views.SEDTypeViewSet)
router.register(r'hostmorphologies', api_views.HostMorphologyViewSet)
router.register(r'phases', api_views.PhaseViewSet)
router.register(r'transientclasses', api_views.TransientClassViewSet)
router.register(r'classicalnighttypes', api_views.ClassicalNightTypeViewSet)
router.register(r'informationsources', api_views.InformationSourceViewSet)
router.register(r'webappcolors', api_views.WebAppColorViewSet)
router.register(r'units', api_views.UnitViewSet)

router.register(r'dataquality', api_views.DataQualityViewSet)

router.register(r'transientfollowups', api_views.TransientFollowupViewSet)
router.register(r'hostfollowups', api_views.HostFollowupViewSet)
router.register(r'hosts', api_views.HostViewSet)
router.register(r'hostseds', api_views.HostSEDViewSet)
router.register(r'instruments', api_views.InstrumentViewSet)
router.register(r'instrumentconfigs', api_views.InstrumentConfigViewSet)
router.register(r'configelements', api_views.ConfigElementViewSet)
router.register(r'logs', api_views.LogViewSet)
router.register(r'transientobservationtasks', api_views.TransientObservationTaskViewSet)
router.register(r'hostobservationtasks', api_views.HostObservationTaskViewSet)
router.register(r'observatories', api_views.ObservatoryViewSet)
router.register(r'oncalldates', api_views.OnCallDateViewSet)

router.register(r'transientphotometry', api_views.TransientPhotometryViewSet, base_name='transientphotometry')
router.register(r'hostphotometry', api_views.HostPhotometryViewSet, base_name='hostphotometry')
router.register(r'transientphotdata', api_views.TransientPhotDataViewSet, base_name='transientphotdata')
router.register(r'hostphotdata', api_views.HostPhotDataViewSet, base_name='hostphotdata')

router.register(r'transientimages', api_views.TransientImageViewSet)
router.register(r'hostimages', api_views.HostImageViewSet)
router.register(r'photometricbands', api_views.PhotometricBandViewSet)
router.register(r'principalinvestigators', api_views.PrincipalInvestigatorViewSet)
router.register(r'profiles', api_views.ProfileViewSet)

router.register(r'transientspectra', api_views.TransientSpectrumViewSet, base_name='transientspectrum')
router.register(r'hostspectra', api_views.HostSpectrumViewSet, base_name='hostspectrum')
router.register(r'transientspecdata', api_views.TransientSpecDataViewSet, base_name='transientspecdata')
router.register(r'hostspecdata', api_views.HostSpecDataViewSet, base_name='hostspecdata')

router.register(r'tooresources', api_views.ToOResourceViewSet, base_name='tooresource')
router.register(r'queuedresources', api_views.QueuedResourceViewSet, base_name='queuedresource')
router.register(r'classicalresources', api_views.ClassicalResourceViewSet, base_name='classicalresource')
router.register(r'classicalobservingdates', api_views.ClassicalObservingDateViewSet, base_name='classicalobservingdate')

router.register(r'telescopes', api_views.TelescopeViewSet)
router.register(r'transients', api_views.TransientViewSet)
router.register(r'alternatetransientnames', api_views.AlternateTransientNamesViewSet)
router.register(r'users', api_views.UserViewSet)
router.register(r'groups', api_views.GroupViewSet)
router.register(r'transienttags', api_views.TransientTagViewSet)

router.register(r'gwcandidates', api_views.GWCandidateViewSet)
router.register(r'gwcandidateimages', api_views.GWCandidateImageViewSet)

# Login/Logout
api_url_patterns = [url(r'^api/', include(router.urls)),
					url(r'^api/schema/$', schema_view),
					url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),]

urlpatterns += api_url_patterns
