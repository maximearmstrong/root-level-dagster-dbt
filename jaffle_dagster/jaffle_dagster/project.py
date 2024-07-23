from pathlib import Path

from dagster_dbt import DbtProject
from dagster_dbt.dbt_project import using_dagster_dev

if using_dagster_dev():
    project_dir = Path(__file__).joinpath("..", "..", "..", "jaffle_shop").resolve()
else:
    project_dir = Path(__file__).joinpath("..", "..", "jaffle_shop").resolve()

jaffle_shop_project = DbtProject(
    project_dir=project_dir,
    packaged_project_dir=Path(__file__).joinpath("..", "..", "dbt-project").resolve(),
)
jaffle_shop_project.prepare_if_dev()
