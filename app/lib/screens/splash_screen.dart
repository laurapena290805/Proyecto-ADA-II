import 'package:app/utils/app_styles.dart';
import 'package:flutter/material.dart';
import 'dart:async';

class SplashScreen extends StatefulWidget {
  const SplashScreen({super.key});

  @override
  _SplashScreenState createState() => _SplashScreenState();
}

class _SplashScreenState extends State<SplashScreen>
    with SingleTickerProviderStateMixin {
  late AnimationController _controller;
  late Animation<double> _fadeInOutAnimation;
  late Animation<double> _scaleAnimation;

  @override
  void initState() {
    super.initState();

    // Configurar controlador de animación
    _controller = AnimationController(
      vsync: this,
      duration: const Duration(seconds: 4), // Duración total de la animación
    );

    // Animación de desvanecimiento: entrada y salida continuas
    _fadeInOutAnimation = TweenSequence([
      TweenSequenceItem(
          tween: Tween<double>(begin: 0.0, end: 0.8), weight: 50), // Aparecer
      TweenSequenceItem(
          tween: Tween<double>(begin: 0.8, end: 0.0),
          weight: 50), // Desaparecer
    ]).animate(
      CurvedAnimation(
        parent: _controller,
        curve: Curves.easeInOut,
      ),
    );

    // Animación de zoom: entrada y salida continuas
    _scaleAnimation = TweenSequence([
      TweenSequenceItem(
          tween: Tween<double>(begin: 0.8, end: 1.0), weight: 50), // Zoom in
      TweenSequenceItem(
          tween: Tween<double>(begin: 1.0, end: 1.2), weight: 50), // Zoom out
    ]).animate(
      CurvedAnimation(
        parent: _controller,
        curve: Curves.easeInOut,
      ),
    );

    // Iniciar la animación
    _controller.forward();

    // Navegar a la HomeScreen después de 4 segundos, cuando termina la animación
    Timer(const Duration(seconds: 4), () {
      Navigator.of(context).pushReplacementNamed('/home');
    });
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.white, // Fondo blanco como Unity
      body: Center(
        child: FadeTransition(
          opacity: _fadeInOutAnimation, // Efecto de desvanecimiento
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              // Icono del robot
              ScaleTransition(
                scale: _scaleAnimation, // Efecto de zoom
                child: const Icon(
                  Icons.android, // Puedes cambiar este ícono por cualquier otro
                  size: 100,
                  color: AppStyles.primaryColor, // Color del ícono
                ),
              ),
              const SizedBox(height: 20), // Espacio entre el ícono y el texto

              // Texto con efecto de zoom también
              ScaleTransition(
                scale: _scaleAnimation,
                child: const Text(
                  'LSL TEAM',
                  style: TextStyle(
                    fontSize: 40,
                    fontWeight: FontWeight.bold,
                    color: AppStyles.primaryColor,
                    letterSpacing: 2.0,
                  ),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
