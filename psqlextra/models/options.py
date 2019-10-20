from typing import Dict, List, Optional, Union

from django.db.models.query import QuerySet

from psqlextra.types import PostgresPartitioningMethod


class PostgresPartitionedModelOptions:
    """Container for :see:PostgresPartitionedModel options.

    This is where attributes copied from the model's `PartitioningMeta`
    are held.
    """

    def __init__(self, method: PostgresPartitioningMethod, key: List[str]):
        self.method = method
        self.key = key
        self.original_attrs: Dict[
            str, Union[PostgresPartitioningMethod, List[key]]
        ] = dict(method=method, key=key)


class PostgresViewOptions:
    """Container for :see:PostgresView and :see:PostgresMaterializedView
    options.

    This is where attributes copied from the model's `ViewMeta` are
    held.
    """

    def __init__(self, query: Optional[QuerySet]):
        self.query = query
        self.original_attrs: Dict[str, Optional[QuerySet]] = dict(
            query=self.query
        )
