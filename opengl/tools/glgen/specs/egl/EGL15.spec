EGLSync eglCreateSync ( EGLDisplay dpy, EGLenum type, const EGLAttrib *attrib_list )
EGLBoolean eglDestroySync ( EGLDisplay dpy, EGLSync sync )
EGLint eglClientWaitSync ( EGLDisplay dpy, EGLSync sync, EGLint flags, EGLTime timeout )
EGLBoolean eglGetSyncAttrib ( EGLDisplay dpy, EGLSync sync, EGLint attribute, EGLAttrib *value )
// NOTE: native_display isn't actually an EGLAttrib. Using EGLAttrib
// so that the generate creates mostly correct code (do not want a buffer)
// have to manually change cast to (void *) in generated code that calls
// the native function.
EGLDisplay eglGetPlatformDisplay ( EGLenum platform, EGLAttrib native_display, const EGLAttrib *attrib_list )
EGLSurface eglCreatePlatformWindowSurface ( EGLDisplay dpy, EGLConfig config, void *native_window, const EGLAttrib *attrib_list )
EGLSurface eglCreatePlatformPixmapSurface ( EGLDisplay dpy, EGLConfig config, void *native_pixmap, const EGLAttrib *attrib_list )
EGLBoolean eglWaitSync ( EGLDisplay dpy, EGLSync sync, EGLint flags )