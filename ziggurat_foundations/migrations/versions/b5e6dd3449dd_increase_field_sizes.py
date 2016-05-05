"""increase user and token field sized

Revision ID: b5e6dd3449dd
Revises: 57bbf0c387c
Create Date: 2016-05-05 11:00:59.915215

"""
from __future__ import unicode_literals

# revision identifiers, used by Alembic.
revision = 'b5e6dd3449dd'
down_revision = '57bbf0c387c'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.alter_column('external_identities', 'access_token',
                    type_=sa.Unicode(512), existing_type=sa.Unicode(255))
    op.alter_column('external_identities', 'alt_token',
                    type_=sa.Unicode(512), existing_type=sa.Unicode(255))
    op.alter_column('external_identities', 'token_secret',
                    type_=sa.Unicode(512), existing_type=sa.Unicode(255))
    op.alter_column('users', 'user_name',
                    type_=sa.Unicode(32), existing_type=sa.Unicode(128))
    op.alter_column('groups_permissions', 'perm_name',
                    type_=sa.Unicode(30), existing_type=sa.Unicode(64),
                    nullable=False)
    op.alter_column('groups_resources_permissions', 'perm_name',
                    type_=sa.Unicode(50), existing_type=sa.Unicode(64),
                    nullable=False)
    op.alter_column('users_permissions', 'perm_name',
                    type_=sa.Unicode(30), existing_type=sa.Unicode(64),
                    nullable=False)
    op.alter_column('users_resources_permissions', 'perm_name',
                    type_=sa.Unicode(50), existing_type=sa.Unicode(64),
                    nullable=False)

def downgrade():
    pass