"""initial schema setup

Revision ID: 6fcb4dfd3760
Revises: 
Create Date: 2017-02-08 13:57:42.874991

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '6fcb4dfd3760'
down_revision = None
branch_labels = None
depends_on = None

__accounts = """

    CREATE  TABLE IF NOT EXISTS `accounts` (

      `account_id` INT NOT NULL AUTO_INCREMENT ,

      `account_guid` VARCHAR(45) NOT NULL UNIQUE,

      `account_name` VARCHAR(255) NOT NULL ,

      `account_type` ENUM('common_niche', 'enterprise') NOT NULL ,

      `company` VARCHAR(255) NOT NULL ,

      `is_active` TINYINT(1) NOT NULL DEFAULT false ,

      `is_deleted` TINYINT(1) NOT NULL DEFAULT false ,

      `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ,

      `updated_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ,

       PRIMARY KEY (`account_id`));

"""

__nerds = """

    CREATE  TABLE IF NOT EXISTS `nerds` (

      `nerd_id` INT NOT NULL AUTO_INCREMENT ,

      `nerd_guid` VARCHAR(45) NOT NULL UNIQUE,

      `account_id` INT NOT NULL ,

      `nerd_name` VARCHAR(255) NOT NULL ,

      `nerd_url` VARCHAR(2083) NOT NULL ,

      `is_active` TINYINT(1) NOT NULL DEFAULT true ,

      `is_deleted` TINYINT(1) NOT NULL DEFAULT false ,

      `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ,

      `updated_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ,

       PRIMARY KEY (`nerd_id`),

       CONSTRAINT `FK_account_nerds`

       FOREIGN KEY (`account_id` )

       REFERENCES `accounts` (`account_id` )

       ON DELETE CASCADE

       ON UPDATE CASCADE);

"""

__users = """

    CREATE  TABLE IF NOT EXISTS `users` (

      `user_id` INT NOT NULL AUTO_INCREMENT ,

      `user_guid` VARCHAR(45) NOT NULL UNIQUE,

      `email` VARCHAR(255) NOT NULL ,

      `password` VARCHAR(255) NOT NULL ,

      `first_name` VARCHAR(255) NOT NULL ,

      `last_name` VARCHAR(255) NOT NULL ,

      `company` VARCHAR(255) NOT NULL ,

      `is_system` TINYINT(1) NOT NULL DEFAULT false ,

      `is_active` TINYINT(1) NOT NULL DEFAULT true ,

      `is_deleted` TINYINT(1) NOT NULL DEFAULT false ,

      `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ,

      `updated_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ,

       PRIMARY KEY (`user_id`));

"""

__account_users = """

    CREATE  TABLE IF NOT EXISTS `account_users` (

      `account_id` INT NOT NULL ,

      `user_id` INT NOT NULL,

      `permission` VARCHAR(255) NOT NULL,

       CONSTRAINT `FK_account_users_account`

       FOREIGN KEY (`account_id` )

       REFERENCES `accounts` (`account_id` )

       ON DELETE CASCADE

       ON UPDATE CASCADE,

       CONSTRAINT `FK_account_users_user`

       FOREIGN KEY (`user_id` )

       REFERENCES `users` (`user_id` )

       ON DELETE CASCADE

       ON UPDATE CASCADE);

"""

__nerd_users = """

    CREATE  TABLE IF NOT EXISTS `nerd_users` (

      `nerd_id` INT NOT NULL ,

      `user_id` INT NOT NULL,

       CONSTRAINT `FK_nerd_users_nerd`

       FOREIGN KEY (`nerd_id` )

       REFERENCES `nerds` (`nerd_id` )

       ON DELETE CASCADE

       ON UPDATE CASCADE,

       CONSTRAINT `FK_nerd_users_user`

       FOREIGN KEY (`user_id` )

       REFERENCES `users` (`user_id` )

       ON DELETE CASCADE

       ON UPDATE CASCADE);

"""


def upgrade():
    op.execute(__accounts)
    op.execute(__nerds)
    op.execute(__users)
    op.execute(__account_users)
    op.execute(__nerd_users)


def downgrade():
    op.execute('DROP TABLE `accounts`;')
    op.execute('DROP TABLE `nerds`;')
    op.execute('DROP TABLE `users`;')
    op.execute('DROP TABLE `account_users`;')
    op.execute('DROP TABLE `nerd_users`;')
