"""empty message

Revision ID: 493fbf11ad78
Revises: ab260562c80a
Create Date: 2025-03-24 20:12:06.700553

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '493fbf11ad78'
down_revision = 'ab260562c80a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('unknown_faces', schema=None) as batch_op:
        batch_op.add_column(sa.Column('age', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('race', sa.String(length=255), nullable=True))
        batch_op.add_column(sa.Column('gender', sa.String(length=255), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('unknown_faces', schema=None) as batch_op:
        batch_op.drop_column('gender')
        batch_op.drop_column('race')
        batch_op.drop_column('age')

    # ### end Alembic commands ###
