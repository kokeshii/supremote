from . import forms

class RemoteFieldFactory(object):

	@staticmethod
	def create(key, field, value, cache):
		initial_value = cache.get(key) or value
		if field['type'] == 'text':
			field_form = forms.RemoteTextField (
				value,
				prefix=key,
				title=field['title'],
				description=field.get('description', ''),
				max_length=field['maxLength'],
				initial=initial_value
			)
				
		elif field['type'] == 'number':
			field_form = forms.RemoteNumberRangeField (
				value,
				prefix=key,
				title=field['title'],
				description=field.get('description', ''),
				choice_range = field['range'],
				initial=initial_value
			)
				
		elif field['type'] == 'boolean':
			field_form = forms.RemoteBooleanField (
				value,
				prefix=key,
				title=field['title'],
				description=field.get('description', ''),
				default_choice = field['default'],
				initial=initial_value
			)
			
		elif field['type'] == 'multiple':
			field_form = forms.RemoteMultipleField (
				value,
				prefix = key,
				title = field['title'],
				description=field.get('description', ''),
				choices = field['choices'],
				initial=initial_value
			)

		return field_form