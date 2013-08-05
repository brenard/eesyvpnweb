# -*- coding: utf-8 -*-


from biryani1.baseconv import cleanup_line, empty_to_none, not_none, pipe, struct


inputs_to_certs_data = struct(
    {
        'state': pipe(cleanup_line, empty_to_none),
        'type': pipe(cleanup_line, empty_to_none),
    },
    default='drop',
    drop_none_values=False,
    )

inputs_to_cert_data = struct(
    {
        'id': pipe(cleanup_line, empty_to_none),
        'action': pipe(cleanup_line, empty_to_none),
        'name': pipe(cleanup_line, empty_to_none),
    },
    default='drop',
    drop_none_values=False,
    )
