from django import forms

class CoeffForm(forms.Form):
	init_temperature = forms.FloatField(required=True, label="Initial Temperature", help_text="Farenheit")
	final_temperature = forms.FloatField(required=True, label="Final Temperature", help_text="Farenheit")
	time_elapsed = forms.IntegerField(label="Time Elapsed", help_text="Minutes")
	surrounding_temperature = forms.FloatField(required=True, label="Surrounding Temperature", help_text="Farenheit")

class FinalTemp(forms.Form):
	time_elapsed = forms.IntegerField(label="Time Elapsed", help_text="Seconds")