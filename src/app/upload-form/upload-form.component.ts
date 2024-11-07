import { Component } from '@angular/core';
import { FormBuilder, FormGroup, ReactiveFormsModule } from '@angular/forms';
import { MatCardModule } from '@angular/material/card';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { MatButtonModule } from '@angular/material/button';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-upload-form',
  standalone: true,
  imports: [
    CommonModule,
    ReactiveFormsModule,
    MatCardModule,
    MatFormFieldModule,
    MatInputModule,
    MatButtonModule
  ],
  templateUrl: './upload-form.component.html',
  styleUrls: ['./upload-form.component.css']
})
export class UploadFormComponent {
  uploadForm: FormGroup;
  selectedFile: File | null = null;
  downloadUrl: string | null = null;

  constructor(private fb: FormBuilder) {
    this.uploadForm = this.fb.group({});
  }

  onFileSelect(event: Event): void {
    const input = event.target as HTMLInputElement;
    if (input.files?.length) {
      this.selectedFile = input.files[0];
      console.log("Selected video file:", this.selectedFile);
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
      this.simulateBackendProcess();
    }
  }

  private simulateBackendProcess(): void {
    setTimeout(() => {
      this.downloadUrl = 'assets/3-Oxlsxccupation_rotation_J2_Vide.xlsx'; 
    }, 2000);
  }
}