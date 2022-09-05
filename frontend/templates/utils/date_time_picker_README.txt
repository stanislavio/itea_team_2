HOW TO ADD DATETIME PICKER TO FORMS:
1. jQuery and jquery.datetimepicker.full.min.js should be included to the page (at the moment done in base.html)
2. date_time_picker_script.html should be included after form as
    {% include 'utils/date_time_picker_script.html' %}
3. Ensure that fields which need picker to be connected have class "date-time-picker-needed". As seen in example forms.py (CreateTrainingPostForm)
    self.fields['datetime_started'].widget.attrs['class'] = 'form-control date-time-picker-needed'
4. Submit button on the form should have id - submit_butto or run following snipped after inclusion of the date_time_picker_script.html:
    $("#submit_button").click(
        change_date_time_fields_to_ISO
    ); //$("#submit_button").click(

    change the id of the submit button
4. Step #3 changes fields to ISO format (in UTC time zone)
5. In Model form (example - CreateTrainingPostForm) create clean function for the appropriate field. Can use parseISOFormatOrNone helper function or write own.


Note: Django does not understand summer savings times. So currently 26Aug2022 it can only use EET timezone for Kyiv, not EEST. For this it registers all dates as UTC+3 instead of +2.



Example files:
1. ModelForms: forms.py (field attributes and cleaninig parsing of date)
2. HTML template - create_training_post.html