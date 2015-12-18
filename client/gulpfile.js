var gulp = require('gulp');
var gutil = require('gulp-util');
var runSequence = require('run-sequence');
var bower = require('gulp-bower');

var basePaths = {
    src: './app/',
    dest: './dist/'
};

// Path
var PATH = {
    html: {
        src: basePaths.src,
        dest: basePaths.dest
    },
    styles: {
        src: basePaths.src + 'css/',
        dest: basePaths.dest + 'css/'
    },
    scripts: {
        src: basePaths.src + 'scripts/',
        dest: basePaths.dest + 'js/'
    },
    bower: {
        dest: basePaths.dest + 'vendor/'
    }
};

var appFiles = {
    html: PATH.html.src + '*.html',
    styles: PATH.styles.src + '*.css',
    scripts: PATH.scripts.src + '**/*.js',
};

gulp.task('scripts', function() {
  return gulp.src(appFiles.scripts)
    .pipe(gulp.dest(PATH.scripts.dest));
});

gulp.task('html', function () {
  return gulp.src(appFiles.html)
    .pipe(gulp.dest(PATH.html.dest));
});

gulp.task('styles', function () {
  return gulp.src(appFiles.styles)
    .pipe(gulp.dest(PATH.styles.dest));
});

gulp.task('build', function (cb) {
  runSequence(['scripts', 'html', 'styles', 'bower'], cb);
});

gulp.task('bower', function() {
  return bower()
    .pipe(gulp.dest(PATH.bower.dest))
});

gulp.task('develop', ['build'], function () {
    gulp.watch(appFiles.html, ['html']);
    gulp.watch(appFiles.scripts, ['scripts']);
});
