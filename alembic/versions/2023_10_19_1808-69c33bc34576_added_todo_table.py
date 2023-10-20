"""Added ToDo table

Revision ID: 69c33bc34576
Revises: a72429c2b1eb
Create Date: 2023-10-19 18:08:52.083906

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '69c33bc34576'
down_revision: Union[str, None] = 'a72429c2b1eb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('todos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=40), nullable=False),
    sa.Column('description', sa.String(length=150), nullable=True),
    sa.Column('status', sa.Boolean(), nullable=False),
    sa.Column('created_at', sa.Date(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('todos')
    # ### end Alembic commands ###