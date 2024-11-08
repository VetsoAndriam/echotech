import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import axios, { AxiosInstance } from 'axios';

@Injectable({
  providedIn: 'root',
})
export class DataService {
    private axiosInstance: AxiosInstance;
  private apiUrl = 'http://localhost:3000'; 

  constructor() {
    this.axiosInstance = axios.create({
      baseURL: this.apiUrl,
      headers: {
        'Authorization': `Bearer ${localStorage.getItem('token')}`,
      },
    });
  }

  /**
   * Envoyer une vidéo au serveur et récupérer un CSV
   * @param videoFile Fichier vidéo
   * @returns Promesse résolvant un Blob
   */
  async uploadVideo(videoFile: File): Promise<Blob> {
    const formData = new FormData();
    formData.append('video', videoFile);

    try {
      const response = await this.axiosInstance.post('/upload-video', formData, {
        responseType: 'blob',
        headers: { 'Content-Type': 'multipart/form-data' },
      });
      return response.data;
    } catch (error) {
      console.error('Erreur lors de l\'envoi de la vidéo :', error);
      throw error;
    }
  }
}