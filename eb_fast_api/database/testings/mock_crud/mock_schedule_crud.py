from unittest.mock import patch
from typing import Optional
from eb_fast_api.database.sources.crud.cruds import ScheduleCRUD


def patcher_schedule_crud_read_all(return_value: Optional[dict]):
    def mock_def_schedule_crud_read_all(
        self,
        userEmail: str,
    ) -> Optional[dict]:
        return return_value

    patcher = patch.object(
        ScheduleCRUD,
        "read_all",
        new=mock_def_schedule_crud_read_all,
    )

    return patcher
