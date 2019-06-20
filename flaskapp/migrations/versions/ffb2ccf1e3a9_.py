"""empty message

Revision ID: ffb2ccf1e3a9
Revises: 3ce8e191bacb
Create Date: 2019-06-20 04:44:23.028639

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ffb2ccf1e3a9'
down_revision = '3ce8e191bacb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
	with op.batch_alter_table('user') as batch_op:
		batch_op.drop_column('rm')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('rm', sa.INTEGER(), nullable=True))
    # ### end Alembic commands ###
