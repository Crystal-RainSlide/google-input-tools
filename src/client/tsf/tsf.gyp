{
  'variables': {
    'srcs': [
      'candidates.cc',
      'candidates.h',
      'compartment.cc',
      'compartment.h',
      'composition_event_sink.cc',
      'composition_event_sink.h',
      'context_event_sink.cc',
      'context_event_sink.h',
      'context_manager.cc',
      'context_manager.h',
      'debug.cc',
      'debug.h',
      'display_attribute.cc',
      'display_attribute.h',
      'display_attribute_manager.cc',
      'display_attribute_manager.h',
      'edit_session.h',
      'external_candidate_ui.cc',
      'external_candidate_ui.h',
      'key_event_sink.cc',
      'key_event_sink.h',
      'language_bar_button.cc',
      'language_bar_button.h',
      'registrar.cc',
      'registrar.h',
      'sink_advisor.h',
      'text_range.cc',
      'text_range.h',
      'text_service.cc',
      'text_service.h',
      'thread_manager_event_sink.cc',
      'thread_manager_event_sink.h',
      'tsf_utils.cc',
      'tsf_utils.h',
      '<(DEPTH)/text_range/edit_ctrl_text_range.cc',
      '<(DEPTH)/text_range/edit_ctrl_text_range.h',
      '<(DEPTH)/text_range/html_text_range.cc',
      '<(DEPTH)/text_range/html_text_range.h',
      '<(DEPTH)/text_range/window_utils.cc',
      '<(DEPTH)/text_range/window_utils.h',
    ],
  },
  'targets': [
    {
      'target_name': 'tsf',
      'type': '<(library)',
      'dependencies': [
        '<(DEPTH)/base/base.gyp:base',
        '<(DEPTH)/ipc/protos/protos.gyp:protos-cpp',
      ],
      'sources': [
        '<@(srcs)',
      ],
    },
    {
      'target_name': 'tsf_x64',
      'type': '<(library)',
      'dependencies': [
        '<(DEPTH)/base/base.gyp:base_x64',
        '<(DEPTH)/ipc/protos/protos.gyp:protos-cpp_x64',
      ],
      'sources': [
        '<@(srcs)',
      ],
    },
  ],
}
