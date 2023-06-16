""" This will be kept in sync with the corresponding Promoted repos.

Note that the following may not be buildable outside the larger Promoted codebase
context, but is provided for visibility and discussion.

PRs are still welcome and Promoted engineers will be happy to test and iterate,
or refine proposed updates.
"""

import analytics.introspection_pull_report.introspection_report_layout_configs.report_layout_groups as g

from analytics.introspection_pull_report.introspection_report_layout_configs.report_layout_formats import (
    Formats,
)
from analytics.introspection_pull_report.introspection_report_layout_configs.report_layout_config import (
    BasicReportConfig,
)

# Including the platform name here is not required, but helpful for clarity
sample_default_report = BasicReportConfig(
    layout_config_display_name="sample_default_report",
    frozen_label_columns=g.default_frozen_label_columns,
    # The default set includes a link here, so we'll just omit it unless
    # we have something we want to replace it with.
    unfrozen_label_columns=(),
    properties_and_selected_columns=(
        g.default_execution_position,
        g.default_retrieval_score,
        g.default_retrieval_rank,
        g.default_blender_score,
        g.default_predictions,
        g.default_counters,
    ),
    dynamic_column_format=g.default_dynamic_column_format,
    # Adding a custom formatted note before our standard header
    # the content of the row is added in the report class itself.
    frozen_label_rows=(
        (
            {
                "ids": ("sample_note",),
                "format": {
                    "cell_format": {
                        "font_color": "#f1c232",
                        "bg_color": "#803763",
                    },
                },
            },
        )
        + g.default_frozen_label_rows
    ),
    frozen_importance_rows=g.default_frozen_importance_rows,
    floating_ranking_end_row=g.default_floating_ranking_end_row,
)
