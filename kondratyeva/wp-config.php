<?php
/**
 * The base configuration for WordPress
 *
 * The wp-config.php creation script uses this file during the installation.
 * You don't have to use the website, you can copy this file to "wp-config.php"
 * and fill in the values.
 *
 * This file contains the following configurations:
 *
 * * Database settings
 * * Secret keys
 * * Database table prefix
 * * ABSPATH
 *
 * @link https://developer.wordpress.org/advanced-administration/wordpress/wp-config/
 *
 * @package WordPress
 */

// ** Database settings - You can get this info from your web host ** //
/** The name of the database for WordPress */
define( 'DB_NAME', 'kondratyeva' );

/** Database username */
define( 'DB_USER', 'root' );

/** Database password */
define( 'DB_PASSWORD', 'root' );

/** Database hostname */
define( 'DB_HOST', 'localhost' );

/** Database charset to use in creating database tables. */
define( 'DB_CHARSET', 'utf8mb4' );

/** The database collate type. Don't change this if in doubt. */
define( 'DB_COLLATE', '' );

/**#@+
 * Authentication unique keys and salts.
 *
 * Change these to different unique phrases! You can generate these using
 * the {@link https://api.wordpress.org/secret-key/1.1/salt/ WordPress.org secret-key service}.
 *
 * You can change these at any point in time to invalidate all existing cookies.
 * This will force all users to have to log in again.
 *
 * @since 2.6.0
 */
define( 'AUTH_KEY',         '-S2i4zcBI(n[mgo6?Z6+,g7m5)[u>[?cMEQjmJr$&=UoKP2KI$z!>I.LKoufz47E' );
define( 'SECURE_AUTH_KEY',  '7r|S|td6$k;Gm,)5@Uhf~PUj$jAa:qq$*bH@0FaOU[;CjrT5<eB63Eo/Yd)&g1J6' );
define( 'LOGGED_IN_KEY',    '>(C.CsmVtGa)JSIpJ)e*P4_SDeULpAMGM87($(0=lLVr/Wk5a:Lo#qOqHdFYmRgj' );
define( 'NONCE_KEY',        '9t+ssqe_A04|I9moakq`;)k#M>A{`!Dtw^jGNm*tp!T|6RZ:FE;3~O+h2SmLAS8-' );
define( 'AUTH_SALT',        'hP%_a24*1w:2:cxRgYFNR]m9!ZGN+w=#m}5l6BqlzPAlAG#}4-W:4Fyn{ucJEv@M' );
define( 'SECURE_AUTH_SALT', '9}Imxd>7YeOq`[#`tg8(4@4mX>4.@vHUT`>%%q3u?S,|;bKjQ0/Tdu`!N_bYZz 3' );
define( 'LOGGED_IN_SALT',   '|-*0K(M2j/bH24=c5.q?p$/@~#<DE^^J4r6|OpKPW0z-AAZ/Z)7OG7U0+(BDeQAZ' );
define( 'NONCE_SALT',       'a6X_Q&MGoW(*z$+qjkTNFW.T^ pMXQP/pIwTAuEPji)q~:qJ<ZS)%(/zyP)i8^(g' );

/**#@-*/

/**
 * WordPress database table prefix.
 *
 * You can have multiple installations in one database if you give each
 * a unique prefix. Only numbers, letters, and underscores please!
 *
 * At the installation time, database tables are created with the specified prefix.
 * Changing this value after WordPress is installed will make your site think
 * it has not been installed.
 *
 * @link https://developer.wordpress.org/advanced-administration/wordpress/wp-config/#table-prefix
 */
$table_prefix = 'wp_';

/**
 * For developers: WordPress debugging mode.
 *
 * Change this to true to enable the display of notices during development.
 * It is strongly recommended that plugin and theme developers use WP_DEBUG
 * in their development environments.
 *
 * For information on other constants that can be used for debugging,
 * visit the documentation.
 *
 * @link https://developer.wordpress.org/advanced-administration/debug/debug-wordpress/
 */
define( 'WP_DEBUG', false );

/* Add any custom values between this line and the "stop editing" line. */



/* That's all, stop editing! Happy publishing. */

/** Absolute path to the WordPress directory. */
if ( ! defined( 'ABSPATH' ) ) {
	define( 'ABSPATH', __DIR__ . '/' );
}

/** Sets up WordPress vars and included files. */
require_once ABSPATH . 'wp-settings.php';
