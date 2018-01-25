from wagtail.wagtailcore import blocks
from wagtail.wagtailsnippets.blocks import SnippetChooserBlock


class SnippetChooserBlockWithAPIGoodness(SnippetChooserBlock):
    def get_api_representation(self, model_instance, context=None):
        return model_instance.serializable_data()


class WhatDoIDoWithBlock(blocks.StaticBlock):
    class Meta:
        icon = 'bin'
        label = 'What do I do with...'
        admin_text = label


class CollectionScheduleBlock(blocks.StaticBlock):
    class Meta:
        icon = 'bin'
        label = 'Collection Schedule'
        admin_text = label
