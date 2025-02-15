# MIT License
#
# Copyright (c) 2020 Jonathan Zernik
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
"""Add use_tor column to all tables with peer address.

Revision ID: 231b8b35ed2e
Revises: d7538b753a8a
Create Date: 2021-10-09 20:24:46.594377

"""
import sqlalchemy as sa
from alembic import op
from sqlalchemy.sql import expression


# revision identifiers, used by Alembic.
revision = '231b8b35ed2e'
down_revision = 'd7538b753a8a'
branch_labels = None
depends_on = None


def upgrade():
    with op.batch_alter_table('peer', schema=None) as batch_op:
        batch_op.add_column(sa.Column('use_tor', sa.Boolean(
        ), nullable=False, server_default=expression.true()))

    with op.batch_alter_table('received_offer', schema=None) as batch_op:
        batch_op.add_column(sa.Column('peer_use_tor', sa.Boolean(
        ), nullable=False, server_default=expression.true()))

    with op.batch_alter_table('received_payment', schema=None) as batch_op:
        batch_op.add_column(sa.Column('peer_use_tor', sa.Boolean(
        ), nullable=False, server_default=expression.true()))

    with op.batch_alter_table('sent_offer', schema=None) as batch_op:
        batch_op.add_column(sa.Column('peer_use_tor', sa.Boolean(
        ), nullable=False, server_default=expression.true()))

    with op.batch_alter_table('sent_payment', schema=None) as batch_op:
        batch_op.add_column(sa.Column('peer_use_tor', sa.Boolean(
        ), nullable=False, server_default=expression.true()))


def downgrade():
    with op.batch_alter_table('sent_payment', schema=None) as batch_op:
        batch_op.drop_column('peer_use_tor')

    with op.batch_alter_table('sent_offer', schema=None) as batch_op:
        batch_op.drop_column('peer_use_tor')

    with op.batch_alter_table('received_payment', schema=None) as batch_op:
        batch_op.drop_column('peer_use_tor')

    with op.batch_alter_table('received_offer', schema=None) as batch_op:
        batch_op.drop_column('peer_use_tor')

    with op.batch_alter_table('peer', schema=None) as batch_op:
        batch_op.drop_column('use_tor')
