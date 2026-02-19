# Guide d'ajout d'images pour la documentation PAGOC MOOC

## 📁 Emplacement des images

Toutes les images doivent être placées dans le dossier :
```
d:/Kaeyros Jonathan/DOCUMENTATION/asf/source/images/
```

## 🖼️ Images requises

Voici la liste des images nécessaires pour chaque section :

### 1. Introduction (`introduction_user.rst`)
- **Nom requis** : `pagoc_logo.png`
- **Description** : Logo officiel de PAGOC MOOC
- **Format** : PNG avec fond transparent
- **Taille recommandée** : 400x200px minimum

### 2. Connexion (`connexion_user.rst`)
- **Nom requis** : `page_connexion.png`
- **Description** : Capture d'écran de la page de connexion/inscription
- **Format** : PNG
- **Taille recommandée** : 1200x800px

### 3. Dashboard (`dashboard_user.rst`)
- **Nom requis** : `dashboard.png`
- **Description** : Vue du tableau de bord utilisateur
- **Format** : PNG
- **Taille recommandée** : 1200x800px

### 4. Cours (`cours_user.rst`)
- **Nom requis** : `cours_catalogue.png`
- **Description** : Capture d'écran du catalogue des cours
- **Format** : PNG
- **Taille recommandée** : 1200x800px

### 5. Mon Apprentissage (`mon_apprentissage_user.rst`)
- **Nom requis** : `mon_apprentissage.png`
- **Description** : Vue de l'espace "Mon Apprentissage"
- **Format** : PNG
- **Taille recommandée** : 1200x800px

### 6. À Propos (`a_propos_user.rst`)
- **Nom requis** : `a_propos.png`
- **Description** : Page "À Propos" avec mission et partenaires
- **Format** : PNG
- **Taille recommandée** : 1200x800px

### 7. Contact (`contact_user.rst`)
- **Nom requis** : `contact.png`
- **Description** : Page de contact avec formulaire
- **Format** : PNG
- **Taille recommandée** : 1200x800px

## 📝 Syntaxe d'insertion des images

Dans les fichiers .rst, les images sont insérées avec cette syntaxe :

```rst
.. image:: images/nom_de_l_image.png
   :alt: Texte alternatif pour l'image
   :align: center
   :scale: 60
```

## ⚙️ Configuration Sphinx

La configuration dans `conf.py` a été mise à jour :
```python
html_static_path = ['_static', 'images']
```

## 🔄 Reconstruction après ajout d'images

Après avoir ajouté les images dans le dossier `images/`, reconstruisez la documentation :

```bash
cd "d:/Kaeyros Jonathan/DOCUMENTATION/asf"
sphinx-build -b html source build
```

## ✅ Vérification

Les images apparaîtront dans :
- `build/html/_images/` (fichiers copiés)
- Pages HTML correspondantes

## 📋 Checklist d'ajout

- [ ] Placer toutes les images dans `source/images/`
- [ ] Vérifier les noms exacts des fichiers
- [ ] S'assurer que les formats sont PNG ou JPG
- [ ] Reconstruire la documentation
- [ ] Vérifier l'affichage dans les pages HTML

## 🎯 Conseils

1. **Qualité** : Utilisez des images haute résolution mais optimisées
2. **Format** : PNG pour les logos, JPG pour les captures d'écran
3. **Taille** : Gardez les fichiers < 500KB pour un chargement rapide
4. **Noms** : Utilisez uniquement des minuscules et underscores
