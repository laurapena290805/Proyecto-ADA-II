import 'package:app/screens/terminal_inteligenteUI.dart';
import 'package:flutter/material.dart';
import '../utils/app_styles.dart';
import 'subasta_publicaUI.dart';

class HomeScreen extends StatelessWidget {
  const HomeScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Center(
        child: Container(
          width: MediaQuery.of(context).size.width *
              0.8, // Ancho 80% del ancho de la pantalla
          height: MediaQuery.of(context).size.height *
              0.6, // Alto 60% del alto de la pantalla
          padding: const EdgeInsets.all(16.0),
          decoration: BoxDecoration(
            color: Colors.white, // Fondo blanco o cualquier color que prefieras
            borderRadius: BorderRadius.circular(20), // Bordes redondeados
            boxShadow: [
              BoxShadow(
                color: Colors.black.withOpacity(0.1),
                blurRadius: 10,
                offset: const Offset(0, 5),
              ),
            ], // Sombra para darle efecto de tarjeta elevada
          ),
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              // Título
              Text(
                'PROYECTO ADA',
                style: AppStyles.titleTextStyle.copyWith(
                  fontSize: 28,
                ),
              ),
              const SizedBox(height: 40),

              // Botones
              ConstrainedBox(
                constraints: const BoxConstraints(minWidth: 250),
                child: Column(
                  children: [
                    // Botón de Subasta Pública
                    ElevatedButton.icon(
                      onPressed: () {
                        // Navegación a la pantalla de Subasta Pública
                        Navigator.of(context).push(
                          MaterialPageRoute(
                            builder: (context) => const SubastaPublicaUI(),
                          ),
                        );
                      },
                      icon: const Icon(
                        Icons.gavel,
                        size: 40,
                        color: Color.fromARGB(255, 69, 133, 136),
                      ),
                      label: const Text(
                        'Subasta Pública',
                        style: AppStyles.buttonTextStyle,
                      ),
                      style: ElevatedButton.styleFrom(
                        backgroundColor: AppStyles.primaryColor,
                        padding: const EdgeInsets.symmetric(
                            horizontal: 60, vertical: 20),
                        minimumSize: const Size.fromHeight(60),
                      ),
                    ),
                    const SizedBox(height: 20),

                    // Botón de Terminal Inteligente
                    ElevatedButton.icon(
                      onPressed: () {
                        // Navegación a la pantalla de Terminal Inteligente
                        Navigator.of(context).push(
                          MaterialPageRoute(
                            builder: (context) => const TerminalInteligenteUI(),
                          ),
                        );
                      },
                      icon: const Icon(
                        Icons.computer,
                        size: 40,
                        color: Color.fromARGB(255, 55, 106, 95),
                      ),
                      label: const Text(
                        'Terminal Inteligente',
                        style: AppStyles.buttonTextStyle,
                      ),
                      style: ElevatedButton.styleFrom(
                        backgroundColor: AppStyles.secondaryColor,
                        padding: const EdgeInsets.symmetric(
                            horizontal: 60, vertical: 20),
                        minimumSize: const Size.fromHeight(60),
                      ),
                    ),
                  ],
                ),
              ),
              const SizedBox(height: 40),

              // Texto de copyright
              const Text(
                '© Laura C, Santiago, Laura P',
                style: TextStyle(
                  fontSize: 14,
                  fontStyle: FontStyle.italic,
                  color: Colors.grey,
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
