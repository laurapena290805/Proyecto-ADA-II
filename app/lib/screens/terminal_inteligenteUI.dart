// ignore_for_file: file_names

import 'package:app/utils/app_styles.dart';
import 'package:flutter/material.dart';

class TerminalInteligenteUI extends StatefulWidget {
  const TerminalInteligenteUI({super.key});

  @override
  _TerminalInteligenteUIState createState() => _TerminalInteligenteUIState();
}

class _TerminalInteligenteUIState extends State<TerminalInteligenteUI> {
  String titulo = 'Elige un método'; // Título inicial
  String subtitulo = 'Asignaciones de Acciones'; // Subtítulo inicial

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.grey[200], // Fondo gris
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          children: [
            _buildBarraFlotante(), // Barra flotante en la parte superior
            const SizedBox(
                height: 16), // Espacio entre la barra flotante y el menú
            Expanded(
              child: Row(
                children: [
                  _buildMenuIzquierdo(), // Menú en la izquierda
                  const SizedBox(
                      width: 16), // Espacio entre el menú y el contenido
                  _buildPanelContenido(), // Panel principal de información
                ],
              ),
            ),
          ],
        ),
      ),
    );
  }

  // Barra flotante estilo AppBar elevado
  Widget _buildBarraFlotante() {
    return Material(
      borderRadius: BorderRadius.circular(16), // Bordes redondeados
      child: Container(
        padding: const EdgeInsets.symmetric(vertical: 1.0, horizontal: 10.0),
        decoration: BoxDecoration(
          color: AppStyles.primaryColor,
          borderRadius: BorderRadius.circular(16),
        ),
        child: Row(
          children: [
            IconButton(
              icon: const Icon(Icons.arrow_back),
              color: AppStyles.buttonTextStyle.color,
              onPressed: () {
                Navigator.pop(context); // Volver a HomeScreen
              },
            ),
            const Spacer(),
            AnimatedSwitcher(
              duration: const Duration(milliseconds: 500),
              child: Text(titulo,
                  key: ValueKey(titulo),
                  style: AppStyles.buttonTextStyle
                      .copyWith(fontSize: 20, fontWeight: FontWeight.w300)),
            ),
            const Spacer(),
          ],
        ),
      ),
    );
  }

  // Menú Izquierdo
  Widget _buildMenuIzquierdo() {
    return Container(
      width: 200, // Ancho del menú
      decoration: BoxDecoration(
        color: Colors.white,
        borderRadius: BorderRadius.circular(16),
      ),
      child: Column(
        children: [
          _buildTituloMenu(),
          const SizedBox(height: 10),
          _buildBotonesSolucion(),
          const Spacer(),
          _buildIconoDecorativo(),
        ],
      ),
    );
  }

  // Título del menú con animación
  Widget _buildTituloMenu() {
    return Container(
      width: 200, // Ancho del menú
      padding: const EdgeInsets.symmetric(vertical: 10.0, horizontal: 15.0),
      decoration: BoxDecoration(
        color: AppStyles.secondaryColor,
        borderRadius: BorderRadius.circular(16),
      ),
      child: Center(
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text(
              'Subasta Pública',
              style: AppStyles.buttonTextStyle.copyWith(
                fontSize: 25,
              ),
            ),
            Text(
              subtitulo,
              style: AppStyles.infomationTextStyle
                  .copyWith(fontSize: 14, color: Colors.white),
            ),
            const SizedBox(height: 7),
          ],
        ),
      ),
    );
  }

  // Botones para los métodos de solución
  Widget _buildBotonesSolucion() {
    return Column(
      children: [
        _buildBotonSolucion('Dinámica', Icons.analytics, () {
          setState(() {
            titulo = 'Método Dinámico';
          });
        }),
        _buildBotonSolucion('Fuerza Bruta', Icons.memory, () {
          setState(() {
            titulo = 'Método Fuerza Bruta';
          });
        }),
        _buildBotonSolucion('Voraz', Icons.flash_on, () {
          setState(() {
            titulo = 'Método Voraz';
          });
        }),
      ],
    );
  }

  // Botón de solución con hover effect
  Widget _buildBotonSolucion(String texto, IconData icono, VoidCallback onTap) {
    return MouseRegion(
      onEnter: (_) =>
          setState(() {}), // Cambios visuales cuando el cursor entra
      onExit: (_) => setState(() {}), // Cambios visuales cuando el cursor sale
      child: InkWell(
        onTap: onTap,
        child: Padding(
          padding: const EdgeInsets.symmetric(vertical: 10.0, horizontal: 16.0),
          child: Row(
            children: [
              Icon(icono, color: AppStyles.primaryColor),
              const SizedBox(width: 8),
              Text(texto, style: const TextStyle(fontSize: 16)),
            ],
          ),
        ),
      ),
    );
  }

  // Icono decorativo al final del menú
  Widget _buildIconoDecorativo() {
    return const Padding(
      padding: EdgeInsets.only(bottom: 16.0),
      child: Icon(Icons.android, size: 50, color: AppStyles.primaryColor),
    );
  }

  // Panel de contenido donde cambia la información según el botón seleccionado
  Widget _buildPanelContenido() {
    return Expanded(
      child: Material(
        borderRadius: BorderRadius.circular(16),
        child: Container(
          padding: const EdgeInsets.all(16.0),
          decoration: BoxDecoration(
            color: Colors.white,
            borderRadius: BorderRadius.circular(16),
          ),
          child: Center(
            child: Text(
              'Contenido relacionado con $titulo',
              style: AppStyles.titleTextStyle.copyWith(fontSize: 20),
            ),
          ),
        ),
      ),
    );
  }
}
