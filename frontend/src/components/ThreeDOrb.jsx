import React, { useEffect, useRef } from 'react';
import * as THREE from 'three';

export default function ThreeDOrb() {
  const containerRef = useRef(null);
  const sceneRef = useRef(null);

  useEffect(() => {
    if (!containerRef.current) return;

    // Scene setup
    const scene = new THREE.Scene();
    sceneRef.current = scene;

    const camera = new THREE.PerspectiveCamera(
      75,
      window.innerWidth / window.innerHeight,
      0.1,
      1000
    );
    camera.position.z = 2;

    const renderer = new THREE.WebGLRenderer({
      antialias: true,
      alpha: true,
    });
    renderer.setSize(window.innerWidth, window.innerHeight);
    renderer.setClearColor(0x000000, 0.1);
    containerRef.current.appendChild(renderer.domElement);

    // Create main orb (sphere with gradient)
    const geometry = new THREE.IcosahedronGeometry(1, 16);
    const material = new THREE.MeshPhongMaterial({
      color: 0x6366f1,
      emissive: 0x6366f1,
      emissiveIntensity: 0.3,
      shininess: 100,
      wireframe: false,
    });

    const sphere = new THREE.Mesh(geometry, material);
    scene.add(sphere);

    // Create wireframe overlay
    const wireframeGeometry = new THREE.IcosahedronGeometry(1.02, 16);
    const wireframeMaterial = new THREE.MeshBasicMaterial({
      color: 0xec4899,
      wireframe: true,
      linewidth: 1,
    });
    const wireframe = new THREE.Mesh(wireframeGeometry, wireframeMaterial);
    scene.add(wireframe);

    // Add lights
    const light1 = new THREE.PointLight(0x6366f1, 1, 100);
    light1.position.set(5, 5, 5);
    scene.add(light1);

    const light2 = new THREE.PointLight(0xec4899, 0.8, 100);
    light2.position.set(-5, -5, 5);
    scene.add(light2);

    const ambientLight = new THREE.AmbientLight(0xffffff, 0.3);
    scene.add(ambientLight);

    // Create particles around orb
    const particlesGeometry = new THREE.BufferGeometry();
    const particleCount = 100;
    const positions = new Float32Array(particleCount * 3);

    for (let i = 0; i < particleCount * 3; i += 3) {
      positions[i] = (Math.random() - 0.5) * 6;
      positions[i + 1] = (Math.random() - 0.5) * 6;
      positions[i + 2] = (Math.random() - 0.5) * 6;
    }

    particlesGeometry.setAttribute('position', new THREE.BufferAttribute(positions, 3));

    const particlesMaterial = new THREE.PointsMaterial({
      color: 0xa5b4fc,
      size: 0.02,
      sizeAttenuation: true,
    });

    const particles = new THREE.Points(particlesGeometry, particlesMaterial);
    scene.add(particles);

    // Animation loop
    let animationFrameId;
    const animate = () => {
      animationFrameId = requestAnimationFrame(animate);

      // Rotate sphere and wireframe
      sphere.rotation.x += 0.0003;
      sphere.rotation.y += 0.0005;
      wireframe.rotation.x -= 0.0002;
      wireframe.rotation.y -= 0.0004;

      // Animate particles
      if (particles.geometry.attributes.position) {
        particles.geometry.attributes.position.array.forEach((val, i) => {
          if (i % 3 === 0) {
            particles.geometry.attributes.position.array[i] += Math.sin(Date.now() * 0.0001 + i) * 0.0005;
          }
        });
        particles.geometry.attributes.position.needsUpdate = true;
      }

      // Pulse effect on sphere
      const time = Date.now() * 0.001;
      material.emissiveIntensity = 0.3 + Math.sin(time) * 0.2;

      renderer.render(scene, camera);
    };

    animate();

    // Handle window resize
    const handleResize = () => {
      const width = window.innerWidth;
      const height = window.innerHeight;
      camera.aspect = width / height;
      camera.updateProjectionMatrix();
      renderer.setSize(width, height);
    };

    window.addEventListener('resize', handleResize);

    // Cleanup
    return () => {
      window.removeEventListener('resize', handleResize);
      cancelAnimationFrame(animationFrameId);
      renderer.dispose();
      geometry.dispose();
      material.dispose();
      wireframeGeometry.dispose();
      wireframeMaterial.dispose();
      particlesGeometry.dispose();
      particlesMaterial.dispose();
      containerRef.current?.removeChild(renderer.domElement);
    };
  }, []);

  return <div ref={containerRef} style={{ width: '100%', height: '100%' }} />;
}