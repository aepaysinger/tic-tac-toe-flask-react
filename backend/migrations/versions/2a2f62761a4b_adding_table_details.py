"""adding table details

Revision ID: 2a2f62761a4b
Revises: 7d00ff3227e0
Create Date: 2023-10-12 10:30:02.062788

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2a2f62761a4b'
down_revision: Union[str, None] = '7d00ff3227e0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('details',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('info', sa.String(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.ForeignKeyConstraint(('user_id',), ['users.id'])
    )

def downgrade() -> None:
    op.drop_table('details')
