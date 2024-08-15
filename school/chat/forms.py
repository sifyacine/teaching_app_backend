from django import forms
from .models import ChatGroup, GroupMessage
from authentication.models import Channel


class ChatmessageCreateForm(forms.ModelForm):
    class Meta:
        model = GroupMessage
        fields = ['body', 'file']

class NewGroupForm(forms.ModelForm):
    class Meta:
        model = ChatGroup
        fields = ['group_name', 'groupchat_name', 'is_private']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['group_name'].label = 'Group Name'
        self.fields['groupchat_name'].label = 'Group Chat Name'
        self.fields['is_private'].label = 'Private Group'

class ChatRoomEditForm(forms.ModelForm):
    remove_members = forms.ModelMultipleChoiceField(
        queryset=Channel.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = ChatGroup
        fields = ['group_name', 'groupchat_name', 'is_private']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['group_name'].label = 'Group Name'
        self.fields['groupchat_name'].label = 'Group Chat Name'
        self.fields['is_private'].label = 'Private Group'
