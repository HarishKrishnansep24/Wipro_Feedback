from django.contrib import admin
from feedback_details.models import trainer_data, trainer_feedback
# from django.db import models
from import_export.admin import ImportExportModelAdmin
from import_export import resources

# admin.site.register(trainer_data)
# admin.site.register(trainer_feedback)


class StudentResource(resources.ModelResource):

    class Meta:
        model = trainer_feedback
        import_id_fields = ('train_id',)
        # exclude = ('id', )
        # fields = ('id','text','option1','option2','option3','option4','answer','section')


class TrainerDataAdmin(ImportExportModelAdmin):
    list_filter = ('communicatin_skill', 'content_delivered',
                   'doubt_clarification', 'technical_skill')
    # list_display = ('train_id.id', 'train_id.name')


admin.site.register(trainer_data)

admin.site.register(trainer_feedback, TrainerDataAdmin)
