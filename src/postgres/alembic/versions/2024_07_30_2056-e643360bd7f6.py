"""empty message

Revision ID: e643360bd7f6
Revises: b49792bf231d
Create Date: 2024-07-30 20:56:03.285469

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e643360bd7f6'
down_revision: Union[str, None] = 'b49792bf231d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('crypto_asset_tags',
    sa.Column('uuid', sa.UUID(), server_default=sa.text('gen_random_uuid()'), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.TIMESTAMP(), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('uuid'),
    sa.UniqueConstraint('name')
    )
    op.create_table('crypto_assets',
    sa.Column('uuid', sa.UUID(), server_default=sa.text('gen_random_uuid()'), nullable=False),
    sa.Column('ticker', sa.String(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('slug', sa.String(), nullable=False),
    sa.Column('cmc_date_added', sa.TIMESTAMP(), nullable=False),
    sa.Column('num_market_pairs', sa.Integer(), nullable=False),
    sa.Column('infinite_supply', sa.Boolean(), nullable=False),
    sa.Column('max_supply', sa.String(), nullable=True),
    sa.Column('cmc_id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.TIMESTAMP(), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('uuid'),
    sa.UniqueConstraint('cmc_id')
    )
    op.create_index(op.f('ix_crypto_assets_name'), 'crypto_assets', ['name'], unique=False)
    op.create_index(op.f('ix_crypto_assets_slug'), 'crypto_assets', ['slug'], unique=False)
    op.create_index(op.f('ix_crypto_assets_ticker'), 'crypto_assets', ['ticker'], unique=False)
    op.create_table('tg_chats',
    sa.Column('uuid', sa.UUID(), server_default=sa.text('gen_random_uuid()'), nullable=False),
    sa.Column('tg_id', sa.BigInteger(), nullable=False),
    sa.Column('type', sa.String(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('username', sa.String(), nullable=True),
    sa.Column('fullname', sa.String(), nullable=True),
    sa.Column('is_forum', sa.Boolean(), server_default=sa.text('false'), nullable=False),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('bio', sa.String(), nullable=True),
    sa.Column('join_by_request', sa.Boolean(), server_default=sa.text('false'), nullable=False),
    sa.Column('invite_link', sa.String(), nullable=True),
    sa.Column('is_removed', sa.Boolean(), server_default=sa.text('false'), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.TIMESTAMP(), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('uuid'),
    sa.UniqueConstraint('tg_id')
    )
    op.create_index(op.f('ix_tg_chats_type'), 'tg_chats', ['type'], unique=False)
    op.create_index(op.f('ix_tg_chats_username'), 'tg_chats', ['username'], unique=False)
    op.create_table('tg_users',
    sa.Column('uuid', sa.UUID(), server_default=sa.text('gen_random_uuid()'), nullable=False),
    sa.Column('tg_id', sa.BigInteger(), nullable=False),
    sa.Column('is_bot', sa.Boolean(), server_default=sa.text('false'), nullable=False),
    sa.Column('first_name', sa.String(), nullable=False),
    sa.Column('last_name', sa.String(), nullable=True),
    sa.Column('username', sa.String(), nullable=True),
    sa.Column('language_code', sa.String(), nullable=True),
    sa.Column('is_premium', sa.Boolean(), server_default=sa.text('false'), nullable=False),
    sa.Column('added_to_attachment_menu', sa.Boolean(), server_default=sa.text('false'), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.TIMESTAMP(), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('uuid'),
    sa.UniqueConstraint('tg_id')
    )
    op.create_table('crypto_asset_quotes',
    sa.Column('id', sa.Integer(), sa.Identity(always=False), nullable=False),
    sa.Column('asset_uuid', sa.UUID(), nullable=False),
    sa.Column('cmc_last_updated', sa.TIMESTAMP(), nullable=False),
    sa.Column('market_cap_dominance', sa.NUMERIC(precision=30, scale=11), nullable=False),
    sa.Column('percent_change_30d', sa.NUMERIC(precision=30, scale=11), nullable=False),
    sa.Column('percent_change_1h', sa.NUMERIC(precision=30, scale=11), nullable=False),
    sa.Column('percent_change_24h', sa.NUMERIC(precision=30, scale=11), nullable=False),
    sa.Column('percent_change_7d', sa.NUMERIC(precision=30, scale=11), nullable=False),
    sa.Column('percent_change_60d', sa.NUMERIC(precision=30, scale=11), nullable=False),
    sa.Column('percent_change_90d', sa.NUMERIC(precision=30, scale=11), nullable=False),
    sa.Column('market_cap', sa.NUMERIC(precision=30, scale=11), nullable=False),
    sa.Column('volume_change_24h', sa.NUMERIC(precision=30, scale=11), nullable=False),
    sa.Column('volume_24h', sa.NUMERIC(precision=30, scale=11), nullable=False),
    sa.Column('price', sa.NUMERIC(precision=30, scale=11), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.TIMESTAMP(), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['asset_uuid'], ['crypto_assets.uuid'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_crypto_asset_quotes_asset_uuid'), 'crypto_asset_quotes', ['asset_uuid'], unique=False)
    op.create_table('crypto_assets_to_asset_tags',
    sa.Column('asset_uuid', sa.UUID(), nullable=False),
    sa.Column('tag_uuid', sa.UUID(), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.TIMESTAMP(), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['asset_uuid'], ['crypto_assets.uuid'], ),
    sa.ForeignKeyConstraint(['tag_uuid'], ['crypto_asset_tags.uuid'], ),
    sa.PrimaryKeyConstraint('asset_uuid', 'tag_uuid')
    )
    op.create_table('crypto_chat_watches',
    sa.Column('uuid', sa.UUID(), server_default=sa.text('gen_random_uuid()'), nullable=False),
    sa.Column('asset_uuid', sa.UUID(), nullable=False),
    sa.Column('tg_chat_uuid', sa.UUID(), nullable=False),
    sa.Column('interval', sa.Enum('EVERY_30_MINUTES', 'EVERY_1_HOUR', 'EVERY_3_HOURS', 'EVERY_6_HOURS', 'EVERY_12_HOURS', 'EVERY_DAY', 'EVERY_WEEK', name='watchinterval', native_enum=False, length=None), nullable=False),
    sa.Column('next_execution_at', sa.TIMESTAMP(), nullable=True),
    sa.Column('created_at', sa.TIMESTAMP(), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.TIMESTAMP(), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['asset_uuid'], ['crypto_assets.uuid'], ),
    sa.ForeignKeyConstraint(['tg_chat_uuid'], ['tg_chats.uuid'], ),
    sa.PrimaryKeyConstraint('uuid'),
    sa.UniqueConstraint('asset_uuid', 'tg_chat_uuid')
    )
    op.create_table('tg_chats_to_users',
    sa.Column('chat_uuid', sa.UUID(), nullable=False),
    sa.Column('user_uuid', sa.UUID(), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.TIMESTAMP(), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['chat_uuid'], ['tg_chats.uuid'], ),
    sa.ForeignKeyConstraint(['user_uuid'], ['tg_users.uuid'], ),
    sa.PrimaryKeyConstraint('chat_uuid', 'user_uuid')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tg_chats_to_users')
    op.drop_table('crypto_chat_watches')
    op.drop_table('crypto_assets_to_asset_tags')
    op.drop_index(op.f('ix_crypto_asset_quotes_asset_uuid'), table_name='crypto_asset_quotes')
    op.drop_table('crypto_asset_quotes')
    op.drop_table('tg_users')
    op.drop_index(op.f('ix_tg_chats_username'), table_name='tg_chats')
    op.drop_index(op.f('ix_tg_chats_type'), table_name='tg_chats')
    op.drop_table('tg_chats')
    op.drop_index(op.f('ix_crypto_assets_ticker'), table_name='crypto_assets')
    op.drop_index(op.f('ix_crypto_assets_slug'), table_name='crypto_assets')
    op.drop_index(op.f('ix_crypto_assets_name'), table_name='crypto_assets')
    op.drop_table('crypto_assets')
    op.drop_table('crypto_asset_tags')
    # ### end Alembic commands ###