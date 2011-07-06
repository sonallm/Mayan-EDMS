from django.utils.translation import ugettext_lazy as _

from navigation.api import register_links, \
    register_model_list_columns, register_multi_item_links, \
    register_sidebar_template

from sources.staging import StagingFile
from sources.models import WebForm, StagingFolder

staging_file_preview = {'text': _(u'preview'), 'class': 'fancybox-noscaling', 'view': 'staging_file_preview', 'args': ['source.source_type', 'source.pk', 'object.id'], 'famfam': 'zoom'}
staging_file_delete = {'text': _(u'delete'), 'view': 'staging_file_delete', 'args': ['source.source_type', 'source.pk', 'object.id'], 'famfam': 'delete'}

setup_web_form_list = {'text': _(u'web forms'), 'view': 'setup_web_form_list', 'famfam': 'application_form'}
setup_web_form_edit = {'text': _(u'edit'), 'view': 'setup_web_form_edit', 'args': 'object.pk', 'famfam': 'application_form_edit'}
setup_web_form_delete = {'text': _(u'delete'), 'view': 'setup_web_form_delete', 'args': 'object.pk', 'famfam': 'application_form_delete'}
setup_web_form_create = {'text': _(u'add new'), 'view': 'setup_web_form_create', 'famfam': 'application_form_add'}

setup_staging_folder_list = {'text': _(u'staging folders'), 'view': 'setup_staging_folder_list', 'famfam': 'folder_magnify'}
setup_staging_folder_edit = {'text': _(u'edit'), 'view': 'setup_staging_folder_edit', 'args': 'object.pk', 'famfam': 'folder_edit'}
setup_staging_folder_delete = {'text': _(u'delete'), 'view': 'setup_staging_folder_delete', 'args': 'object.pk', 'famfam': 'folder_delete'}
setup_staging_folder_create = {'text': _(u'add new'), 'view': 'setup_staging_folder_create', 'famfam': 'folder_add'}

source_list = {'text': _(u'Document sources'), 'view': 'setup_web_form_list', 'famfam': 'page_add'}

register_links(StagingFile, [staging_file_preview, staging_file_delete])

register_links(['setup_web_form_list', 'setup_web_form_create', 'setup_staging_folder_list', 'setup_staging_folder_create'], [setup_web_form_list, setup_staging_folder_list], menu_name='form_header')

register_links(WebForm, [setup_web_form_list, setup_staging_folder_list], menu_name='form_header')
register_links(WebForm, [setup_web_form_edit, setup_web_form_delete])
register_links(['setup_web_form_list', 'setup_web_form_edit', 'setup_web_form_delete', 'setup_web_form_create'], [setup_web_form_create], menu_name='sidebar')

register_links(StagingFolder, [setup_web_form_list, setup_staging_folder_list], menu_name='form_header')
register_links(StagingFolder, [setup_staging_folder_edit, setup_staging_folder_delete])
register_links(['setup_staging_folder_list', 'setup_staging_folder_edit', 'setup_staging_folder_delete', 'setup_staging_folder_create'], [setup_staging_folder_create], menu_name='sidebar')

source_views = ['setup_web_form_list', 'setup_web_form_edit', 'setup_web_form_delete', 'setup_web_form_create', 'setup_staging_folder_list', 'setup_staging_folder_edit', 'setup_staging_folder_delete', 'setup_staging_folder_create']
