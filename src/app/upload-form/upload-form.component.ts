import { Component } from '@angular/core';
import { FormBuilder, FormGroup, ReactiveFormsModule } from '@angular/forms';
import { MatCardModule } from '@angular/material/card';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { MatButtonModule } from '@angular/material/button';
import { CommonModule } from '@angular/common';
import { DataService } from '../data.service';
import { saveAs } from 'file-saver';

@Component({
  selector: 'app-upload-form',
  standalone: true,
  imports: [
    CommonModule,
    ReactiveFormsModule,
    MatCardModule,
    MatFormFieldModule,
    MatInputModule,
    MatButtonModule,
  
  ],
  templateUrl: './upload-form.component.html',
  styleUrls: ['./upload-form.component.css']
})
export class UploadFormComponent {
  uploadForm: FormGroup;
  selectedFile: File | null = null;
  downloadUrl: string | null = null;
  data: object[] = [];

  constructor(private fb: FormBuilder, private dataService: DataService) {
    this.uploadForm = this.fb.group({});
  }

  onFileSelect(event: Event): void {
    const input = event.target as HTMLInputElement;
    if (input.files?.length) {
      this.selectedFile = input.files[0];
      console.log("Selected video file:", this.selectedFile);
      this.data = [
        { name: 'Example', size: this.selectedFile.size, type: this.selectedFile.type }
      ];
    }
  }

  onFileDrop(event: DragEvent): void {
    event.preventDefault();
    if (event.dataTransfer?.files.length) {
      this.selectedFile = event.dataTransfer.files[0];
      console.log("Dropped file:", this.selectedFile);
    }
  }

  onDragOver(event: DragEvent): void {
    event.preventDefault();
  }

  onSubmit(): void {
    if (this.selectedFile) {
      this.uploadFile();
    }
  }

  async  uploadFile(): Promise<void> {
    if (!this.selectedFile) {
      console.error('Aucun fichier sélectionné.');
      return;
    }

    try {
      const csvBlob = await this.dataService.uploadVideo(this.selectedFile);
      saveAs(csvBlob, 'output.csv'); 
      console.log('CSV téléchargé avec succès.');
    } catch (error) {
      console.error('Erreur lors de l\'upload ou du téléchargement :', error);
    }
  }
}