# YOLO_v8
 Thực hiện chương trình nhận diện hoa quả với 3 loại quả phân biệt: cam, bưởi, chanh
## Dữ liệu
Tập dữ liệu hiện có chỉ bao gồn cam (tốt) và cam (hỏng)
## Các file trained
best_20, best_40 là các file pretrained từ yolo8s.pt được training trên tập dữ liệu cam, chuối, táo, v.v bổ xung thêm
kết quả trained được mô tả tại result 20- result 40

## Chương trình chạy
run_pro là file chạy nhận diẹn test trên camera laptop với cpu, run_pro_img là nhận diện trên ảnh
start_train là file truyền thông số cho quá trình trainning thay vì nhận trong CLI
start_val thực hiện đánh giá trên bộ validation
tutorial_tinker là giao diện người dùng theo mẫu BTL môn học

## Các hình ảnh đã nhận diện (minh hoạ)
