from rest_framework import serializers
from labelit.models import Project, ProjectTask, Task
from labelit.serializers import TaskPolymorphicSerializer, TaskSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model


# TODO: DRY vs. ./user_serializer.py
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = [
            "id",
            "first_name",
            "last_name",
        ]


class ProjectSerializer(serializers.ModelSerializer):
    tasks = TaskPolymorphicSerializer(many=True, required=False)
    created_by = UserSerializer(many=False, required=False)
    created_at = serializers.DateTimeField(
        format="%Y-%m-%d", required=False, read_only=True
    )
    updated_at = serializers.DateTimeField(
        format="%Y-%m-%d", required=False, read_only=True
    )

    class Meta:
        model = Project
        fields = [
            "id",
            "name",
            "is_audio_annotated",
            "is_text_annotated",
            "task_presentation",
            "enable_region_annotation",
            "are_sequences_annotated",
            "tasks",
            "timer_inactivity_threshold",
            "archived",
            "do_display_timer_time",
            "does_audio_playing_count_as_activity",
            "target_deadline",
            "target_num_documents",
            "description",
            "created_at",
            "updated_at",
            "created_by",
        ]


class FlatProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = [
            "id",
            "name",
            "is_audio_annotated",
            "is_text_annotated",
            "enable_region_annotation",
            "are_sequences_annotated",
            "tasks",
            "timer_inactivity_threshold",
            "archived",
            "do_display_timer_time",
            "does_audio_playing_count_as_activity",
            "target_deadline",
            "target_num_documents",
            "description",
            "created_at",
            "updated_at",
            "created_by",
        ]

        extra_kwargs = {"created_by": {"default": serializers.CurrentUserDefault()}}

    def create(self, validated_data):
        project = Project.objects.create(**validated_data)
        request = self.context.get("request")
        task_ids = request.data.get('tasks')
        for idx, t_id in enumerate(task_ids):
            ProjectTask.objects.create(
                project=project,
                task_id=t_id,
                order=idx + 1
            )

        return project


class ProjectWithStatsSerializer(serializers.ModelSerializer):
    tasks = TaskPolymorphicSerializer(many=True, required=False)
    num_documents = serializers.SerializerMethodField()
    num_done_documents = serializers.SerializerMethodField()
    num_done_batches = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = [
            "id",
            "name",
            "is_audio_annotated",
            "is_text_annotated",
            "enable_region_annotation",
            "are_sequences_annotated",
            "tasks",
            "timer_inactivity_threshold",
            "num_documents",
            "num_done_documents",
            "num_done_batches",
            "archived",
            "target_num_documents",
            "target_deadline",
            "description",
            "do_display_timer_time",
            "does_audio_playing_count_as_activity",
            "description",
        ]

    def get_num_documents(self, obj):
        return obj.get_num_documents()

    def get_num_done_documents(self, obj):
        return obj.get_num_done_documents()

    def get_num_done_batches(self, obj):
        return obj.get_num_done_batches()
